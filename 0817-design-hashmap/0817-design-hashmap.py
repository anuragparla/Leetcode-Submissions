class MyHashMap:

    def __init__(self):
        self.capacity = 10000  # A reasonably large prime number or power of 2 for capacity
        self.buckets = [[] for _ in range(self.capacity)]
        

    def _hash(self, key: int) -> int:
        """
        Helper function to calculate the hash index for a given key.
        """
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        hash_index = self._hash(key)
        bucket = self.buckets[hash_index]

        # Check if the key already exists in the bucket
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update the value
                return
        
        # If key not found, add the new key-value pair
        bucket.append((key, value))

    def get(self, key: int) -> int:
        hash_index = self._hash(key)
        bucket = self.buckets[hash_index]

        # Search for the key in the bucket
        for k, v in bucket:
            if k == key:
                return v
        
        return -1  # Key not found

    def remove(self, key: int) -> None:
        hash_index = self._hash(key)
        bucket = self.buckets[hash_index]

        # Find and remove the key-value pair
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)