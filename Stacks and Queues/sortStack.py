# Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.

from stack import Stack

class StackWithSort(object):
    def __init__(self):
        self.items = []
        self.tempStack = Stack()

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def sort(self):
        self.tempStack = Stack()
        while not self.isEmpty():
            temp = self.pop()
            count = 0
            while not self.tempStack.isEmpty() and self.tempStack.peek() < temp:
                self.push(self.tempStack.pop())
                count += 1
            self.tempStack.push(temp)
            for i in range(0,count):
                self.tempStack.push(self.pop())
        return self.tempStack

    def printSorted(self):
        while not self.tempStack.isEmpty():
            print(self.tempStack.pop())

if __name__ == '__main__':
    test = StackWithSort()
    test.push(4)
    test.push(3)
    test.push(32)
    test.push(30)
    test.push(124)
    test.sort()
    test.printSorted()