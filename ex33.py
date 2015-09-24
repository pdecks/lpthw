# Exercise 33: While-Loops



# def num_list_generator(max_val, incr):
# 	i = 0
# 	numbers = []
# 	while i < max_val:
# 		print "At the top i is %d" % i
# 		numbers.append(i)

# 		i += incr
# 		print "Numbers now: ", numbers
# 		print "At the bottom i is %d" % i

# 	return numbers

# print "Enter a value between 1 and 10."
# max_val_in = int(raw_input("> "))
# print "Enter a step value between 1 and 10."
# step = int(raw_input("> "))

# gen_numbers = num_list_generator(max_val_in, step)

# print "The numbers:"

# for num in gen_numbers:
# 	print num


# rewrite using for-loops and range:
def num_list_generator(max_val): #, incr):
	i = 0
	numbers = []
	for i in range (0, max_val):
		print "At the top i is %d" % i
		numbers.append(i)
		# the increment is no longer needed because i is automatically incremented
		# by 1 in the for-loop
		# i += incr
		print "Numbers now: ", numbers
		
		# print "At the bottom i is %d" % i

	return numbers

print "Enter a value between 1 and 10."
max_val_in = int(raw_input("> "))
#print "Enter a step value between 1 and 10."
#step = int(raw_input("> "))

gen_numbers = num_list_generator(max_val_in) #, step)

print "The numbers:"

for num in gen_numbers:
	print num