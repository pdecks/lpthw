# Exercise 4: Variables and Names

# define number of cars
cars = 100

# define car capacity
space_in_a_car = 4 # it is not necessary to use 4.0 here because we only have an integer number of people

# define number of drivers
drivers = 30

# define number of passengers, including number of drivers
passengers = 90

# calculate idling cars
cars_not_driven = cars - drivers

# calculate driven cars
cars_driven = drivers

# calculate max passengers that can be transported
carpool_capacity = cars_driven * space_in_a_car

# calculate average passengers per car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven,"empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "passengers to carpool today."
print "We need to put about", average_passengers_per_car, "passengers in each car."

# test printing without spaces between words
# print "Hey%sthere." % "you" # prints "Heyyouthere."
# print "Hey % sthere." % "you" # prints "Hey you there."