# Exercise 13, version 2
# takes a script name and two additional arguments

from sys import argv

script, first, second = argv

print """
Your script is called: %s
Your first argument is: %s
Your second argument is: %s
""" % (script, first, second)