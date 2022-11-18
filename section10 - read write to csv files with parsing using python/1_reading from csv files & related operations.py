'''
csv pkg is in-built in Python enables to handle the csv files.
'''

import csv
import os

filepath = 'C:\\Users\\sridh\\PycharmProjects\\pythonProject\\pythonProject\\ApiTestingProject\\utilities\\loanapp.csv'
with open(filepath) as csvfile:
    # method in csv pkg helps in reading contents csv file
    # we give filename and delimter in params
    # This will return a reader object that has all rows
    reader = csv.reader(csvfile, delimiter=',')
    # print(reader)
    # print(list(reader))
    name = input("enter the name -  ")
    # scenario1 - we need a list of names and status separately.
    names, status = [], []
    for row in reader:
        # print(row)
        names.append(row[0])
        status.append(row[1])
    # print("\n names - ", names, "\n status - ", status)

    # scenario2 - find out the status of the application basis on name input
    index = names.index(name)
    print(status[index])