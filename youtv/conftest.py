from datetime import datetime
from pathlib import Path
from youtv.utils.ci_utils import is_running_in_ci
import os
import pytest


home = Path(__file__).resolve().parent
reports_folder = home.joinpath('reports')
driver = None
time_now = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = reports_folder / "report.html"


def _capture_screenshot(name):
    driver.get_screenshot_as_file(os.path.join(reports_folder, name))


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
       Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
       :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            Path(reports_folder).mkdir(parents=True, exist_ok=True)
            file_name = report.nodeid.replace("::", "_").replace("/", "_").replace(".", "_") + "_" + time_now + "_.png"
            _capture_screenshot(file_name)
            if file_name:
                img = '<div><img src="file:%s" ' \
                      'alt="screenshot" style="width:475px;height:243px;" ' \
                      'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(img))
        report.extra = extra

