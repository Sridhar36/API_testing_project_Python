filepath = 'C:\\Users\\sridh\\PycharmProjects\\pythonProject\\pythonProject\\ApiTestingProject\\utilities\\loanapp.csv'
import csv

with open(filepath, 'a') as csvfile:
    # writer method to write to a file
    write = csv.writer(csvfile)
    write.writerow(['Sri', 'approved'])  # to add a new row
    # to write in new row send data in list format.
