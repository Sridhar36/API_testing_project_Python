# if file present in same package as your Python module then we can directly give file name
# else we will need to provide the path of the file

file = open('textfile')
print(file.read())  # To read all the contents of the file
print(file.read(2))  # To read first two  characters of a file | read n characters

# to read line by line
print(file.readline())
file.close()  # whenever you open a file you'll need to close it. It's a good practice

# Q: print line by line using readline method
line = file.readline()
while line != '':
    print(line)
    line = file.readline()

# file.readlines() - stores all the contents of a file in list.. making it easy to work with data in file

for line in file.readlines():
    print(line)