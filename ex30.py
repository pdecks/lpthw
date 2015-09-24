# Exercise 30: Else and If

people = 30
cars = 30
buses = 15

if cars > people:
	print "We should take the cars."
# What happens if multiple elif statements are true?
# Python starts at the top and runs the first block that is True, so it will run only the first one.
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."

if people > buses:
	print "All right. Let's just take the buses."
else:
	print "Fine, let's stay home then."


# more complex versions

if cars > people and people > buses:
	print "All right. Let's just take the buses."
