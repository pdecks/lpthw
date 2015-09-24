# Exercise 11: Asking Questions

print "What's your name?",
name = raw_input()
print "How old are you?",
age = raw_input('(in years) ')
print "How tall are you?",
height = raw_input('(in inches) ')
print "How much do you weigh?",
weight = raw_input('(in pounds) ')

print """
Let's see if I got this right ...
You are %s years old, you are %s inches tall, and you weigh %s pounds.
""" % (age, height, weight)

# Study Drills
print "Where is your hometown?",
hometown = raw_input('(City, State [e.g., Chico, CA] ')
print "What is your favorite color?",
color = raw_input()
print "Who is your favorite author?",
author = raw_input()

print """
Thanks, %s! You grew up in %s, your favorite color is %s,
and you like reading books by %s.
""" % (name, hometown, color, author)