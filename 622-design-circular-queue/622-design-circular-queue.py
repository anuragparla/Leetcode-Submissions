class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k 
        self.head = None
        self.tail = None
        self.size = 0
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:

            node = Node(value)
            if self.tail == None:
                self.size +=1 
                self.tail = node
                self.head = node
            elif self.tail != None:
                oldTail = self.tail
                oldTail.next = node
                node.prev = oldTail 
                self.tail = node
                self.tail.next = self.head
                self.head.prev = self.tail
                self.size +=1 
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
       
        if self.head != None and self.head == self.tail:
            self.head = None
            self.tail = None
            self.size -= 1 
        else:
            oldHead = self.head
            self.tail.next = oldHead.next
            oldHead.next.prev = self.tail
            self.head = oldHead.next
            self.size -= 1
        return True

        

    def Front(self) -> int:

        if self.head != None:
            return self.head.value
        else:
            return -1

    def Rear(self) -> int:
        if self.tail != None:
            return self.tail.value
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if self.size >= self.capacity:
            return True
        else:
            return False
