file = open('textfile')
# file.readlines() - stores all the contents of a file in list.. making it easy to work with data in file

for line in file.readlines():
    print(line)
