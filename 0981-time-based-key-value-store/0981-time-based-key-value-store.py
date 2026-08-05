class TimeMap:

    def __init__(self):
        self.time_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.time_map.get(key,[])
        l , r = 0, len(values) - 1
        res = ""
        while l<=r:
            mid = (l + r) // 2 
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1 

        return res
            


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)