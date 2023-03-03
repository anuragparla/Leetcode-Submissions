class Node:
    def __init__(self ,key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def makeNodeHead(self, node):
        if self.tail == node:
            self.tail.prev.next = None
            node.next = self.head 
            self.head.prev = node
        elif self.head != node:
            currPrev = node.prev
            currNext = node.next
            if(currPrev != None):
                currPrev.next = currNext
            if(currNext != None):
                currNext.prev = currPrev
            node.next = self.head 
            self.head.prev = node 
            self.head = node
        
            
    def removeNodeFromTail(self):
        if self.tail != None:
            self.tail.prev.next = None
    def addToHead(self, node):
        if self.head == None:
            self.head = node
        else:
            self.makeNodeHead(node)

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity   = capacity
        self.map = {}
        self.size = 0
        self.dll = DLL()

    def get(self, key: int) -> int:
        res = -1 
        if key in self.map:
            res = self.map[key].val
        return res 

    def put(self, key: int, value: int) -> None:
                # key already exists 
                if key in self.map:
                    # rewrite the val of key & make that node as head 
                    self.map[key].val = value
                    self.dll.makeNodeHead(self.map[key])
                # key does not exist but capacity is reached 
                elif key not in self.map and self.size>= len(self.map):
                    # remove the tail, add the new key and make it head 
                    self.dll.removeNodeFromTail()
                    node = Node(key,value)
                    self.map[key] = node
                    self.dll.addToHead(node)
                    self.size +=1
                # key does not exist and capacity is not reached  
                else:
                    # add this key val and make it as head 
                    node = Node(key,value)
                    self.map[key] = node
                    self.dll.addToHead(node)
                    self.size +=1 


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
