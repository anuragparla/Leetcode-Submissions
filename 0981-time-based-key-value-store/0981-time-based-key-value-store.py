class TimeMap:

    def __init__(self):
        self.time_map = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.time_map.get(key,[])
        l , r = 0 , len(values) - 1
        while l<=r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res




    
    '''
    i need a ds to store key value pairs 
    here the value is a combination of a string and int timestamp 
    we can probably pair them into a list and they will live in a list i.e list of lists [[],[]] -> O(1)
    get -> we will pass the key and the timestamp. if there is no value for that key return an empty string
    let's say key exists and if the timestamp also exists we can return the value 
    if that timestamp doesn't exist then we need to at least find a timestamp that is lesser than the current timestamp 
    challenge is how do we search if there is multiple timestamp for the same key? 
    also the timestamp will be inserted in an asceding order 
    we can search for the timestamp using binary search
    '''
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)