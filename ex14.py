# Exercise 14: Prompting and Passing

from sys import argv

script, user_name, language = argv

prompt = '> '

if language == 'Italian':
	print "Ciao, %s. Sono %s." % (user_name, script)
	print "Vorrei chiederti alcune domande."
	print "Ti piaccio, %s?" % user_name
	likes = raw_input(prompt)

	print "Dove abiti, %s?" % user_name
	lives = raw_input(prompt)

	print "Che tipo di computer hai?" 
	computer = raw_input(prompt)

	print """
	Bene! Su se ti piaccio, hai dico '%s'.
	Tu abiti nel %s. Non lo so dove.
	Tu hai un %s. Che buono!
	""" % (likes, lives, computer)
	
else:

	print "Hi, %s. I am the %s script." % (user_name, script)
	print "I'd like to ask you a few questions."
	print "Do you like me, %s?" % user_name
	likes = raw_input(prompt)

	print "Where do you live, %s?" % user_name
	lives = raw_input(prompt)

	print "What kind of computer do you have?"
	computer = raw_input(prompt)

	print """
	All right -- you said '%s' about liking me.
	You live in %s. Not sure where that is.
	And you have a %s computer. Nice.
	""" % (likes, lives, computer)