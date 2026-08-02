class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val 
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_cache = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self,node):
        prevNode = node.prev
        nextNode = node.next 
        prevNode.next, nextNode.prev = nextNode, prevNode

    def add(self,node):
        prevNode = self.tail.prev
        prevNode.next = node 
        node.prev = prevNode
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.lru_cache:
            val = self.lru_cache[key].val
            self.remove(self.lru_cache[key])
            self.lru_cache[key] = Node(key,val)
            self.add(self.lru_cache[key])
            return self.lru_cache[key].val
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.lru_cache:
            self.remove(self.lru_cache[key])
            self.lru_cache[key] = Node(key,value)
            self.add(self.lru_cache[key])
        else:
            self.lru_cache[key] = Node(key,value)
            self.add(self.lru_cache[key]) 
        
        if len(self.lru_cache) > self.capacity:
            lru_key = self.head.next.key
            self.remove(self.head.next)
            del self.lru_cache[lru_key]
            

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)