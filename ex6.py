# Exercise 6: Strings and Text
# "programmers love saving themselves some time at your expense by using annoying cryptic variable names..."

# define string 'x', with format string
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # 1st & 2nd place a string is put inside a string

print x
print y

# note %r is used for debugging
print "I said: %r." % x # 3rd place a string is put inside a string
# whereas %s is used for displaying to users
print "I also said: '%s'." % y # 4th place a string is put inside a string

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" 

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# concatenate strings
print w + e
