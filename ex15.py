# Exercise 15: Reading Files

# import the argv module
from sys import argv

# from the command line arguments, assign the script name (arg1) and filename (arg2)
script, filename = argv

# open the file and save it as 'txt'
txt = open(filename)

# print the contents of the file
print "Here's your file %r:" % filename
print txt.read()

# close the file, for good measure
txt.close()
#print "Enter a max number of bytes to read:",
#bytes = int(raw_input())
#print txt.read(bytes)

# this doesn't work...
#print "Let's write something to a new file:"
#filename2 = raw_input("> Enter a filename: ")
#txt_add = raw_input("> Enter some text: ")
#filename2.write(txt_add)

# input the filename using a prompt
print "Type the filename again:"
file_again = raw_input("> ")

# open the file and assign it to the variable 'txt_again'
txt_again = open(file_again)

# print the contents of the file
print txt_again.read()

# close the file
txt_again.close()