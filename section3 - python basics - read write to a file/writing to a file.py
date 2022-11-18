# we can open a file using 'with' keyword, by using this we need not write one more step to close the file.
# Open file in read use r  & to write use w

'''
task:
read the content of file
store in list
reverse the list
write back to file
'''

with open('textfile', 'r') as reader:
    content = reader.readlines()
    reversed(content)  # reversed method will reverse the contents of a list
    with open('textfile', 'w') as writer:
        for line in reversed(content):
            writer.write(line)  #write method writes into the file