# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.

import linkedListImplementation as l

def sumLists(a,b, carry):
	if(a is None and b is None and carry == 0):
		return None
	value = carry
	if a is not None:
		value += a.getData()
	if b is not None:
		value += b.getData()
	result = l.Node(value % 10)
	isCarry = 0
	if value >= 10:
		isCarry = 1
	if(a is not None and b is not None):
		more = sumLists(a.getNext(),
						b.getNext(),
						isCarry)
		result.setNext(more)
	return result

if __name__ == "__main__":
	s = l.LinkedList(l.Node(7))
	s.add(l.Node(1))
	s.add(l.Node(6))

	z = l.LinkedList(l.Node(5))
	z.add(l.Node(9))
	z.add(l.Node(2))
	result = sumLists(s.getHead(), z.getHead(), 0)

	w = l.LinkedList(result)
	w.printAll()
