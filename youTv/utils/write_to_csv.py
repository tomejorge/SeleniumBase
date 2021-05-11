from csv import writer
import csv
import datetime


def add_user_data_to_csv(file, mix, email, ):
    """ used to append test data one wants to keep to a csv file """
    with open(file, 'a', newline='') as csvfile:
        fieldnames = ['DATE', 'MIX', 'EMAIL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect="excel")
        today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow({'DATE': today, 'MIX': mix, 'EMAIL': email})
        csvfile.close()


def append_to_csv_2(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)
