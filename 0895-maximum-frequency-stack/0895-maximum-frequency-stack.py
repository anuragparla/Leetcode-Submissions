class FreqStack:

    def __init__(self):
        self.freq_map = {} # val -> freq
        self.maxCount = 0 
        self.max_freq_stack = {}

    def push(self, val: int) -> None:
        self.freq_map[val] = self.freq_map.get(val,0) + 1 
        valCount = self.freq_map[val]
        if valCount > self.maxCount:
            self.maxCount = valCount
        if valCount not in  self.max_freq_stack:
            self.max_freq_stack[valCount] = [val]
        else:
            self.max_freq_stack[valCount].append(val)

    def pop(self) -> int:
        res = self.max_freq_stack[self.maxCount].pop()
        self.freq_map[res] -= 1
        if not self.max_freq_stack[self.maxCount]:
            self.maxCount -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()