# Exercise 25: Even More Practice

# Instead of running this file, import it into Python and run the functions

def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

my_sentence = "The quick brown fox took a nap next to a mossy log."

broken = break_words(my_sentence)
print "This is break_words(sentence):"
print broken
print "\n"

print "This is sort_words(words):"
print sort_words(broken)
print "\n"

print "This is print_first_word(words):"
print_first_word(broken)
print "\n"

print "This is print_last_word(words):"
print_last_word(broken)
print "\n"

sort_sent = sort_sentence(my_sentence)
print "This is sort_sentence(sentence):"
print sort_sent
print "\n"

print "This is print_first_and_last(sentence):"
print_first_and_last(my_sentence)
print "\n"

print "This is print_first_and_last_sorted(sentence):"
print_first_and_last_sorted(my_sentence)
print "\n"