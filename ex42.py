# Learn Python the Hard Way Exercise 42: Is-A, Has-A, Objects, and Classes

## Animal is-a object
class Animal(object):
	
	legs = 0
	can_speak = False
	sound = ''

	def __init__(self, name):
		self.name = name

	# def can_speak(animal):
	# 	return animal.can_speak()

	def make_sound(sound):
		print self.sound

## Dog is-a Animal
class Dog(Animal):

	legs = 4
	can_speak = False
	sound = 'woof!'

	#def __init__(self, name):
		## Dog has-a attribute name that is equal to parameter name
	#	self.name = name

## Cat is-a Animal
class Cat(Animal):

	legs = 4
	can_speak = False
	sound = 'meow!'

	# def __init__(self, name):
	# 	## Cat has-a attribute name that is equal to parameter name
	# 	self.name = name

## Person is-a object
class Person(Animal):

	legs = 2
	can_speak = True
	sound = 'yee-haw!'

	def __init__(self, name):
		## Person has-a attribute name that is set to parameter name
		#self.name = name
		super(Person, self).__init__(name)
		## Person has-a pet
		self.pet = None

## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		# Employee inherits the __init__ from Person
		super(Employee, self).__init__(name)
		## Employee has-a attribute salary equal to parameter salary
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")
print "The dog has %d legs" % rover.legs
print "The dog is named %s" % rover.name
print "Can the dog speak? %r" % rover.can_speak
print "The dog goes %s" % rover.sound
rover.make_sound()


## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")
print "Can %s speak? %r" % (mary.name, mary.can_speak)

## mary has-a pet cat named Satan
mary.pet = satan

## frank is-a employee who earns $120k
frank = Employee("Frank", 120000)

## frank has-a pet dog named Rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()