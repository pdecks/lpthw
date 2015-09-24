# Exercise 16: Reading and Writing Files

# makes a simple text editor

from sys import argv

# pass the script name and filename from the commandline
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want to do that, hit CTRL-C (^C)." #^C is "KeyboardInterrupt"
print "If you want to proceed, hit RETURN."

raw_input("?")

# open the file (file object = target)
print "Opening the file..."
target = open(filename, 'w')

# truncate the file
print "Truncating the file. Goodbye!"
target.truncate()

# collect input from user to write to file
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# write the lines to the file
print "I'm going to write these to the file."

write_string = "%s\n%s\n%s\n" % (line1, line2, line3)
target.write(write_string) #% (line1, line2, line3)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

# close the file
print "And finally, we close the file."
target.close()
