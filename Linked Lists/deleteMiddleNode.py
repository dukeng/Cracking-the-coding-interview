# Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.


import linkedListImplementation
# see imported file for linkedList reference



#Copy the value of middleNode->next to middleNode and point middleNode.next = middleNode.next.next 
def deleteMiddleNode(middleNode):
	middleNode.setData(middleNode.getNext().getData())
	middleNode.setNext(middleNode.getNext().getNext())

if __name__ == "__main__":
	s = linkedListImplementation.LinkedList(linkedListImplementation.Node(0))
	s.add(linkedListImplementation.Node(3))
	s.add(linkedListImplementation.Node(4))
	s.add(linkedListImplementation.Node(5))
	s.add(linkedListImplementation.Node(6))
	s.add(linkedListImplementation.Node(8))
	print("Before: ")
	s.printAll()
	middleNode = s.getHead().getNext().getNext().getNext()
	print("Middle node is ", middleNode.getData())
	deleteMiddleNode(middleNode)
	print("After: ")
	s.printAll()
