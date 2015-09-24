# Exercise 19 Study Drill - create your own function and run it 10 ways

def dogs_or_cats(animal_type, num_of_animal):
	if num_of_animal > 1:
		animal_plural = animal_type + 's'
	else:
		animal_plural = animal_type
	if animal_type == 'dog':
		print "Dogs rule, and cats drool!"	
	else:
		print "Cats rule, and dogs drool!"
	print "I have %d %s. Got a problem with that?" % (num_of_animal, animal_plural)

dogs_or_cats('dog', 10)

dogs_or_cats('dog', 2 - 1)

dogs_or_cats('cat', 1 + 1 * 20)