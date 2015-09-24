# Exercise 19b : More Functionality

def pet_lover():
	print "What is your favorite animal?"
	animal = raw_input("> ")
	print "How many bedrooms do you have in your home?"
	num_animal = int(raw_input("> "))

	if num_animal > 1:
		animal_plural = animal + 's'
	else:
		animal_plural = animal
	print "You should adopt %d %s!" % (num_animal, animal_plural)

pet_lover()

pet_lover()

pet_lover()

pet_lover()

pet_lover()

pet_lover()

pet_lover()

pet_lover()

pet_lover()

pet_lover()
