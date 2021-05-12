import os


# check if we are running in CI
def is_running_in_ci():
    return os.environ.get('CI') is not None
