# Learn Python The Hard Way Exercise 44 Inheritance vs. Composition
# final version that shows each kind of interaction from inheritance in one go

class Parent(object):

	def override(self):
		print "PARENT override()"

	def implicit(self):
		print "PARENT implicit()"

	def altered(self):
		print "PARENT altered()"


class Child(Parent):

	def override(self):
		print "CHILD override()"

	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"


dad = Parent()
son = Child()

print "-- OVERRIDE --"
print 'dad:'
dad.override()
print 'son:'
son.override()

print "-- IMPLICIT --"
print 'dad:'
dad.implicit()
print 'son:'
son.implicit()

print "-- ALTERED --"
print 'dad:' 
dad.altered()
print 'son:'
son.altered()