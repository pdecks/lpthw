# Learn Python The Hard Way: Exercise 41 - Learning to Speak Object Oriented

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

# define key/phrase pairs
# %%% --> class
# *** --> instance, function ('other')
# @@@ --> parameter
PHRASES = {
	"class %%%(%%%):":
	  "Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)":
	  "class %%% has-a __init__ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self, @@@)": 
	  "class %%% has-a function named *** that takes self and @@@ parameters.",
	"*** = %%%()":
	  "Set *** to an instance of class %%%.",
	"***.***(@@@)":
	  "From *** get the *** function, and call it withopen parameters self, @@@.",
	"***.*** = '***'":
	  "From *** get the *** attribute and set it to '***'."
}

# prompt user for type of drill -- phrases vs. keys
PHRASE_FIRST = False

print "Which would you like to drill, CODE or ENGLISH?"
choice = raw_input("> ")

if choice == "ENGLISH":
	PHRASE_FIRST = True

# load the words from the website
for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip())

# create a function that determines the number of substitutions for each pair
# and randomly assigns words from the word list
def convert(snippet, phrase):
	class_names = [w.capitalize() for w in 
	               random.sample(WORDS, snippet.count("%%%"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []

	# randomly create # of paramaters
	for i in range (0, snippet.count("@@@")):
		param_count = random.randint(1, 3)
		param_names.append(', '.join(random.sample(WORDS, param_count)))
		# print param_names ... one item in the list because lists are 
		# mutable but strings are not?

	# make a copy of the snippet-phrase pair (python copy of a list)
	for sentence in snippet, phrase:
		result = sentence[:]

		# make substitutions
		# fake class names
		for word in class_names:
			result = result.replace("%%%", word, 1)

		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)

		# fake parameter names
		for word in param_names:
			result = result.replace("@@@", word, 1)

		results.append(result)

	return results

# keep drilling until the user hits CTRL-D to exit
try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(snippets)

		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question

			print question

			raw_input("> ")
			print "ANSWER: %s\n\n" % answer
except EOFError:
	print "\nBye"