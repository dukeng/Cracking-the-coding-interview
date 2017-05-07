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
        return self.head

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