

class ThreeStack():
    def __init__(self, length):
        self.length = length
        self.array = [None for i in range(length)]
        self.pointers = [0, length // 3, (length // 3) * 2]

    def isEmpty(self,num):
        if self.pointers[num] == num * self.length // 3:
            return True
        else:
            return False

    def push(self, num, item):
        if self.pointers[num] < self.length // 3 * (num + 1):
           self.array[self.pointers[num]] = item
           self.pointers[num] += 1
        else:
            raise Exception("StackOverFlow")

    def pop(self,num):
        ret = None
        if not self.isEmpty(num):
            ret = self.array[self.pointers[num]]
            self.pointers[num] -= 1
        return ret

    def peek(self, num):
        ret = None
        if not self.isEmpty(num):
            ret = self.array[self.pointers[num] - 1]
        return ret

    def size(self, num):
        return self.pointers[num] - (self.length // 3 * num ) 


if __name__ == '__main__':
    stack = ThreeStack(30)
    stack.push(0, 99)
    stack.push(0, 98)
    print(stack.peek(0))