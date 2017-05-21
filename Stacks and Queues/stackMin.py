# Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.


class MinStack:
    def __init__(self):
        self.items = []
        self.min = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        if self.min[-1] > item:
        	self.min.append(item)

    def pop(self):
    	if self.min[-1] == item:
    		self.min.pop()
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def min(self):
        if len(self.min) != 0:
            return self.min[-1]
