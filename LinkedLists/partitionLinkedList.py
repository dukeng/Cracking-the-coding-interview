# Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. lf x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.

import linkedListImplementation as l

def traverse(head):
	pass

def append(linkedList, element):
	# head = linkedList.getHead()
	# if head is None:
	# 	linkedList.add(l.Node(element))
	# while head is not None:
	# 	head = head.getNext()
	# head = l.Node(element)
	# print(head.getData())
	# print(linkedList.getHead())
	# linkedList.printAll()
	# return linkedList
	linkedList.add(l.Node(element))
	return linkedList

def partitionLinkedList(linkedList, partition):
	head = s.getHead()
	lessThan = l.LinkedList(None)
	equal = l.LinkedList(None)
	greater = l.LinkedList(None)
	while head is not None:
		data = head.getData()
		if data > partition:
			greater.add(l.Node(data))
		elif data == partition:
			equal.add(l.Node(data))
		else:
			lessThan.add(l.Node(data))
		head = head.getNext()

	lessThanPointer = lessThan.getHead()
	equalPointer = equal.getHead()
	while equalPointer is not None:
		greater.add(l.Node(equalPointer.getData()))
		equalPointer = equalPointer.getNext()
	while lessThanPointer is not None:
		greater.add(l.Node(lessThanPointer.getData()))
		lessThanPointer = lessThanPointer.getNext()

	return greater

if __name__ == "__main__":
	s = l.LinkedList(l.Node(3))
	s.add(l.Node(5))
	s.add(l.Node(8))
	s.add(l.Node(4))
	s.add(l.Node(7))
	s.add(l.Node(2))
	s.add(l.Node(1))
	s.printAll()
	print("After")
	partition = 5
	z = partitionLinkedList(s, partition)
	z.printAll()