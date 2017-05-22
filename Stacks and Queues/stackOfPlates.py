# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push () and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop ( ) should return the same values as it would if there were just a single stack).
import stack

class StackSets:
    def __init__(self, num):
        self.items = []
        self.stackList = [stack.Stack() for i in range(num)]
        self.stackPointer = 0
        self.stackSizes = [0 for i in range(num)]
        self.max = 5

    def isEmpty(self):
        if self.stackPointer == 0 and self.stackSizes[self.stackPointer] == 0:
            return False
        return True

    def push(self, item):
        if self.stackSizes[self.stackPointer] >= self.max:
            self.stackPointer += 1
        self.stackSizes[self.stackPointer] += 1
        self.stackList[self.stackPointer].push(item)

    def pop(self):
        if not self.isEmpty():            
            if self.stackSizes[self.stackPointer] == 0:
                self.stackPointer -= 1
            self.stackSizes[self.stackPointer] -= 1
            return self.stackList[self.stackPointer].pop()
        else:
            return None

    def peek(self):
        if not self.isEmpty():            
            if self.stackSizes[self.stackPointer] == 0:
                self.stackPointer -= 1
            return self.stackList[self.stackPointer].peek()
        else:
            return None

    def size(self):
        total = 0
        for stack in self.stackList:
            total += stack.size()
        return total
    def debug(self):
        return self.stackList

if __name__ == '__main__':
    a = StackSets(5)
    a.push(1)
    print(a.pop())
    print(a.peek())
