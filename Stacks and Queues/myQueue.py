# Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.

from stack import Stack

class MyQueue():
	def __init__(self):
		self.oldStack = Stack()
		self.newStack = Stack()

	def isEmpty(self):
		if self.oldStack.isEmpty() and self.newStack.isEmpty():
			return True
		else:
			return False
	def push(self, item):
		self.newStack.push(item)

	def pop(self):
		self.shift()
		return self.oldStack.pop()

	def peek(self):
		self.shift()
		return self.oldStack.peek()

	def shift(self):
		if self.oldStack.isEmpty():
			while not (self.newStack.isEmpty()):
				self.oldStack.push(self.newStack.pop())

if __name__ == '__main__':
	queue = MyQueue()
	queue.push(10)
	print(queue.isEmpty())
	print(queue.peek())