# Implement an algorithm to find the kth to last element of a singly linked list.

class LinkedList(): 
    head = None
    def __init__(self,head):
        self.head = head
    def add(self,data):
        temp = self.head
        while temp.getNext() != None:
            temp = temp.getNext()
        temp.setNext(data)
    def printAll(self):
        temp = self.head
        while temp.getNext() != None:
            print(temp.data)
            temp = temp.getNext()
        print(temp.data) #extra print for the last element
    def getHead(self):
        return self.head;
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
 
def nthToLast(linkedList, k):
    counter = 0
    firstPointer = linkedList.getHead();
    for x in range(k):
        if firstPointer.getNext() != None:
            firstPointer = firstPointer.getNext()
    if firstPointer.getNext() == None:
        print("not possible")
        return 1
    else:
        secondPointer = linkedList.getHead();
        while firstPointer.getNext() != None:
            firstPointer = firstPointer.getNext()
            secondPointer = secondPointer.getNext()
        while secondPointer.getNext() != None:
            print(secondPointer.getData())
            secondPointer = secondPointer.getNext()
# For the above code, the credit goes to http://ls.pwd.io/2014/08/singly-and-doubly-linked-lists-in-python/
# Assume that the linked list's size is unknown, we do this iteratively
if __name__ == "__main__":
    s = LinkedList(Node(0))
    for x in range(4, 20, 1):
        s.add(Node(x))
    # s.printAll()
    nthToLast(s, 5)