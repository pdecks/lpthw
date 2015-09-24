# Exercise 19: Functions and Variables

# define a function that prints the values of the arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man, that's enough for a party!"
	print "Get a blanket.\n"

# pass numbers directly to the function
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"

# define variables to pass to function
amount_of_cheese = 10
amount_of_crackers = 50

# call function using variables instead of numbers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# call function with arithmetic arguments
print "We can even do math inside, too:"
cheese_and_crackers(10 + 20, 5 + 6)

# call function with combined arguments
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)