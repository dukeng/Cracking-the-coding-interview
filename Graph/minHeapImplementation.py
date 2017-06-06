from random import randint

##
# Space   O(n)
# Search  O(n)
# Insert  O(log n)
# Delete  O(log n)
# Reference page: http://algorithms.tutorialhorizon.com/binary-min-max-heap/


class minHeap():
    def __init__(self):
        self.arr = []
    
    def insert(self, element):
        self.arr.append(element)
        child = len(self.arr) - 1 # the recently added index
        parent = int((child - 1)/2) # get the parent index
        while parent >= 0: # bubble up
            if self.arr[parent] > self.arr[child]:
                self.arr[parent], self.arr[child] = self.arr[child], self.arr[parent]
                child = parent
                parent = int((child - 1)/2) # get the parent index
            else:
                break


    def bubble_down(self, parent, leftIndex, rightIndex):
        while True: # bubble down
            if rightIndex < len(self.arr): # 2 children
                swap = leftIndex if self.arr[leftIndex] < self.arr[rightIndex] else rightIndex
                if self.arr[parent] > swap:
                    self.arr[parent], self.arr[swap] = self.arr[swap], self.arr[parent]
                    parent = swap
                    leftIndex = (parent + 1) * 2 - 1
                    rightIndex = (parent + 1) * 2
                else:
                    break
            elif leftIndex < len(self.arr): # 1 left children
                if self.arr[parent] > self.arr[leftIndex]:
                    self.arr[parent], self.arr[leftIndex] = self.arr[leftIndex], self.arr[parent]
                    parent = leftIndex
                    leftIndex = (parent + 1) * 2 - 1
                    rightIndex = (parent + 1) * 2
                else:
                    break
            else: # no children, bottom of tree
                break

    def extractMin(self):
        if len(self.arr) == 0:
            return None
        elif len(self.arr) == 1:
            return self.arr.pop()
        else:
            retVal = self.arr[0]
            self.arr[0] = self.arr.pop()
            parent = 0
            leftIndex = (parent + 1) * 2 - 1
            rightIndex = (parent + 1) * 2
            self.bubble_down(parent, leftIndex, rightIndex)
            return retVal

    def getArray(self):
        return self.arr

    def printArray(self):
        print(self.arr)

    def delete(self, item):
        index = self.arr.index(item)
        if index is not None:
            if len(self.arr) == 1:
                return self.arr.pop()
            else:
                self.arr[index], self.arr[-1] = self.arr[-1], self.arr[index]
                self.arr.pop()
                parent = 0
                leftIndex = (parent + 1) * 2 - 1
                rightIndex = (parent + 1) * 2
                self.bubble_down(parent, leftIndex, rightIndex)
                return self.arr.pop()
        else:
            return None




if __name__ == '__main__':
    minHeap = minHeap()
    minHeap.insert(1)
    minHeap.insert(5)
    minHeap.insert(2)
    minHeap.insert(0)
    minHeap.insert(10)
    minHeap.insert(12)
    minHeap.insert(40)
    minHeap.insert(30)
    minHeap.insert(25)
    minHeap.insert(3)
    minHeap.delete(3)
    print(minHeap.getArray())
    while len(minHeap.getArray()) != 0:
        print(minHeap.extractMin())
