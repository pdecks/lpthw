# Exercise 40: Modules, Classes, and Objects

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
				   "I don't want to get sued",
				   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
					    "With pockets full of shells"])

lonely_holiday = Song(["It was a lonely holiday",
					   "I was alone, you were away",
					   "In Fayetteville or in another state",
					   "There's so many towns I hate",
					   "When you leave me, it breaks me like a bone",
					   "But it's never as bad as when you come home",
					   "I've thought so much about suicide",
					   "Parts of me have already died",
					   "Lonely, baby I'm not lonely",
					   "Baby I'm not, I've got my imaginary frineds",
					   "Happy, baby I'm so happy",
					   "Baby I'm so, I've got my imaginary friends",
					   "And if you don't love me, would you please pretend?"])

bohemian_rhapsody = ["""
Is this the real life? Is this just fantasy? Caught in a landslide
No escape from reality. Open your eyes. Look up to the skies and seeEEEEeeeeEEEEe
"""]

print '-' * 10

happy_bday.sing_me_a_song()

print '-' * 10

bulls_on_parade.sing_me_a_song()

print '-' * 10

lonely_holiday.sing_me_a_song()

print '-' * 10
# print bohemian_rhapsody
queen = Song(bohemian_rhapsody)
queen.sing_me_a_song()