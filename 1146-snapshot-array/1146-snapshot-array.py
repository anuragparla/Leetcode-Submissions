class SnapshotArray:

    def __init__(self, length: int):
        self.history = [[] for _ in range(length)]
        self.snap_id = 0
        
    def set(self, index: int, val: int) -> None:
        self.history[index].append([self.snap_id,val])
        
    def snap(self) -> int:
        sid = self.snap_id 
        self.snap_id +=1
        return sid
        
    def get(self, index: int, snap_id: int) -> int:
        if not self.history[index]:
            return 0
        values = self.history[index]
        res = 0
        l , r = 0, len(values) - 1
        while l<= r:
            mid = (l + r) // 2
            if values[mid][0] <= snap_id:
                res =  values[mid][1]
                l = mid + 1
            else:
                r = mid - 1 
        return res

        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)