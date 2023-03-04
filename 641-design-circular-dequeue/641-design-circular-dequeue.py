class Node:
    def __init__(self, value) -> None:
        self.value = value 
        self.next = None
        self.prev = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k 
        self.size = 0
        self.head = None
        self.tail = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.size +=1
            node = Node(value)
            if self.head == None:
                self.head = node
                self.tail = node 
            else:
                oldHead = self.head
                self.tail.next = node
                node.next = oldHead
                oldHead.prev = node 
                self.head = node 
        return True 

    def insertLast(self, value: int) -> bool:
            if self.isFull():
                return False
            else:
                self.size +=1 
                node = Node(value)
                if self.tail == None:
                    self.head = node 
                    self.tail = node
                else:
                    oldTail = self.tail
                    oldTail.next = node 
                    node.next = self.head
                    self.head.prev = node  
                    node.prev = oldTail
                    self.tail = node
            return True 

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.size -=1 
            if self.head != None and self.head == self.tail: 
                self.head = None 
                self.tail = None
            else:
                oldHead = self.head
                self.tail.next = oldHead.next
                oldHead.next.prev = self.tail 
                self.head = oldHead.next
                
        return True


    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False 
        else:
            self.size -= 1 
            if self.tail != None and self.head == self.tail:
                self.head = None 
                self.tail = None
            else:
                self.tail.prev.next = None
                self.tail = self.tail.prev
        return True 

    def getFront(self) -> int:
        if self.head != None:
            return self.head.value
        else:
            return -1 

    def getRear(self) -> int:
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


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
