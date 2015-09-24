# Exercise 31: Making Decisions

print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> Enter '1' or '2': ")

if door == "1":
	print "There's a giant bear here eating a cheesecake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	print "3. Offer the bear some candy."

	bear = raw_input("> Enter '1', '2', or '3': ")

	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	elif bear == "3":
		print "The bear puts down its fork and looks you in the eye."
		print "'I LOVE candy!' the bear exclaims. 'Would you like some of my cake?'"
		print "1. Accept the bear's offer."
		print "2. Politely decline the bear's offer."

		bear_offer = raw_input("> Enter '1' or '2': ")

		if bear_offer == '1':
			print "You sit down next to the bear and enjoy a piece of cake."
			print "You are starting to feel sleepy. Why don't you take a nap?"
			print "1. Take a nap."
			print "2. Get the heck out of this room with the bear!"

			nap = raw_input("> Enter '1' or '2': ")

			if nap == '1':
				print "As you finally drift of to sleep, you feel a searing pain in"
				print "your side as the bear bites into your full stomach. The bear"
				print "says, 'I only offered you the cake to fatten you up! Yum!'"
				print "YOU ARE DEAD. Good job!"
			elif nap == '2':
				print "While the bear is still enjoying its sweet treat, you tiptoe"
				print "away, back toward whence you came. You wake up and realize ..."
				print "IT WAS ALL A DREAM! Good job!"
			else:
				print "Seriously? You couldn't decide? Well, now you are bear lunch."
				print "YOU ARE DEAD. Good job!"
		elif bear_offer == '2':
			print "The bear is noticably upset by your refusal. The bear stands up on"
			print "its hind legs and roars loudly in your face before biting your head"
			print "off. YOU ARE DEAD. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> Enter '1', '2', or '3': ")

	if insanity == ("1" or "2"):
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"

else:
	print "You stumble around and fall onto a knife and die. Good job!"