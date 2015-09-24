# Exercise 21: Functions can RETURN Something

def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
# extra credit solution
def what_func(a, h, w, i):
	return h - ((i / 2) * w) + a

print "Let's do some math with these functions!"

age = add(30, 3)
height = subtract(72, 6)
weight = multiply(67, 2)
iq = divide(400, 3)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# a puzzle for extra credit, type it in anyway
print "Here is a puzzle."

what = add(age, subtract(height, multiply (weight, divide(iq,2))))

print "That becomes:", what, "Can you do it by hand?"

print "Does this match?", what_func(age, height, weight, iq)