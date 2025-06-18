class MyHashSet:

    def __init__(self):
        #self.bucket = list(1000)
        #self.bucketItem = list(1000)
        self.hashSet = [None]*1000



    def firstHash(self, key) -> int:
        return key % 1000
    
    def secondHash(self, key ) -> int:
        return key // 1000



    def add(self, key: int) -> None:
        bucketIndex = self.firstHash(key)
        print(bucketIndex)
        bucketItemIndex = self.secondHash(key)

        if self.hashSet[bucketIndex] is None:
            if bucketIndex == 0:
                self.hashSet[bucketIndex] = [False] * 1001
            else:
                self.hashSet[bucketIndex] = [False] * 1000
            self.hashSet[bucketIndex][bucketItemIndex] = True
        else:
            self.hashSet[bucketIndex][bucketItemIndex] = True
            
        

    def remove(self, key: int) -> None:
        bucketIndex = self.firstHash(key)
        bucketItemIndex = self.secondHash(key)
        if self.hashSet[bucketIndex] is not None:
            self.hashSet[bucketIndex][bucketItemIndex] = False
    
            
        

    def contains(self, key: int) -> bool:
        bucketIndex = self.firstHash(key)
        bucketItemIndex = self.secondHash(key)
        if self.hashSet[bucketIndex] is None:
            return False
        if self.hashSet[bucketIndex][bucketItemIndex] == True:
            return True
        return False
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)