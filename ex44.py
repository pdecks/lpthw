# Learn Python the Hard Way Exercise 44: Inheritance vs. Composition

# implicit inheritance

class Parent(object):

	def implicit(self):
		print "PARENT implicit()"

class Child(Parent):
	pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()


# override explicitly

class GoodParent(object):

	def override(self):
		print "PARENT override()"


class DisobedientChild(GoodParent):

	def override(self):
		print "CHILD override()"

father = GoodParent()
boy = DisobedientChild()

father.override()
boy.override()


# alter before or after
# first override the function ... but then use 'super()' to get parent version to call'

class MasterParent(object):

	def altered(self):
		print "PARENT altered()"


class AlteredChild(MasterParent):

	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(AlteredChild, self).altered()
		print "CHILD, AFTER PARENT altered()"

dad = MasterParent()
son = AlteredChild()

dad.altered()
son.altered()