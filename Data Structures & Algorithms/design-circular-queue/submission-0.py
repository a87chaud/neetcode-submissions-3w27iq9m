class MyCircularQueue:
    '''
    cap = 3
    currsize = 3 -> en: fail
    [-1, 2, 3]
            ^
            h
    ^
    t
    insert at head
    pop at tail
    '''

    def __init__(self, k: int):
        self.k = k
        self.queue = [-1] * k
        self.head = -1
        self.tail = 0
        self.currSize = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.head = (self.head + 1) % self.k
        self.queue[self.head] = value
        self.currSize += 1
        # print(f'q: {self.queue}')
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.tail] = -1
        self.tail = (self.tail + 1) % self.k
        self.currSize -= 1
        print(f'q: {self.queue}')
        return True
    
    def Front(self) -> int:
        return self.queue[self.tail]    

    def Rear(self) -> int:
        return self.queue[self.head]

    def isEmpty(self) -> bool:
        return self.currSize == 0

    def isFull(self) -> bool:
        return self.currSize == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()