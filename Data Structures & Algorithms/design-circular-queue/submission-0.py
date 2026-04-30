class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.front = -1
        self.rear = -1
        self.queue = [-1] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        # for single element
        if self.front == -1:
            self.front = self.rear = 0

        # for circular conditon when rear is at end
        elif self.rear == self.k - 1 and self.front != 0:
            self.rear = 0

        # normal case
        else:
            self.rear += 1

        # puth the value in queue
        self.queue[self.rear] = value

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        # increament the front and give prev fornt -1
        self.queue[self.front] = -1

        # single element
        if self.front == self.rear:
            self.front = self.rear = -1

        # condition for circular queue, when front is at end of queue
        elif self.front == self.k - 1:
            self.front = 0

        # normal case
        else:
            self.front += 1
        
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return ((self.front == 0 and self.rear == self.k - 1) or
                (self.rear == (self.front - 1 + self.k) % self.k))

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()