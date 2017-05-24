# Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
# out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. Create the data structures to
# maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat. You may use the built-in LinkedList data structure.

class Animal():
	def __init__(self, name, order=0):
		self.name = name
		self.order = order

	def isOlderThan(self, another):
		return self.order < another.getOrder()
	
	def getOrder(self):
		return self.order

	def setOrder(self, order):
		self.order = order

	def toString(self):
		return ( self.name, self.order)

class Dog(Animal):
	def __init__(self, name, order=0):
		super().__init__(name, order)


class Cat(Animal):
	def __init__(self, name, order=0):
		super().__init__(name, order)


class AnimalQueue():
	def __init__(self):
		self.dogs = []
		self.cats = []
		self.order = 0

	def enqueue(self, animal):
		animal.setOrder(self.order)
		self.order += 1
		if animal.__class__.__name__== "Dog":
			self.dogs.append(animal)
		else:
			self.cats.append(animal)

	def dequeueAny(self):
		if len(self.dogs) == 0:
			return self.dequeueCats()
		elif len(self.cats) == 0:
			return self.dequeueDogs()
		dog = self.dogs[-1]
		cat = self.cats[-1]
		if dog.isOlderThan(cat):
			return self.dequeueDogs()
		else:
			return self.dequeueCats()
	
	def dequeueDogs(self):
		if not len(self.dogs) == 0:
			return self.dogs.pop(0)
	def dequeueCats(self):
		if not len(self.cats) == 0:
			return self.cats.pop(0)


if __name__ == '__main__':
	animalQueue = AnimalQueue()
	animalQueue.enqueue(Dog("test2"))
	animalQueue.enqueue(Dog("test3"))
	animalQueue.enqueue(Dog("test4"))
	animalQueue.enqueue(Dog("test5"))
	animalQueue.enqueue(Cat("test6"))
	animalQueue.enqueue(Cat("test7"))
	animalQueue.enqueue(Cat("test8"))
	animalQueue.enqueue(Cat("test9"))
	print(animalQueue.dequeueAny().toString())
	print(animalQueue.dequeueAny().toString())
	print(animalQueue.dequeueCats().toString())
	print(animalQueue.dequeueCats().toString())
	print(animalQueue.dequeueDogs().toString())
