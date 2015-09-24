# Exercise 5: More Variables and Printing
# in this exercise you will learn how to make strings that have variables embedded in them --> format strings!

my_name = 'Patricia L. Decker'
my_age = 33 # not a lie
my_height = 66 # inches
my_weight = 133 # lbs
my_eyes = 'Green'
my_teeth = 'White'
my_hair = 'Platinum'
inches_to_cm = 2.54
pounds_to_kilos = 1 / 2.2

print "Let's talk about %s." % my_name
print "She's %d inches tall, which is %d cm tall." % (my_height, my_height * inches_to_cm)
print "She weighs %d pounds, which is %f kilos." % (my_weight, my_weight * pounds_to_kilos)
print "Actually, we'd better not talk about weight today."
print "She's got %s eyes and %s hair." % (my_eyes, my_hair)
print "Her teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

# here is the %r format character
print "Print %r no matter what!" % my_name
print "Print %r no matter what!" % my_age