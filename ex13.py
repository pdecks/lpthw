# Exercise 13: Parameters. Unpacking. Variables.

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# alternatively ...
print """
The script is called: %s
Your first variable is: %s
Your second variable is: %s
Your third variable is: %s
""" % (script, first, second, third)