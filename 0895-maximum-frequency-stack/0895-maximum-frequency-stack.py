class FreqStack:

    def __init__(self):
        self.cnt = {}
        self.maxCnt = 0
        self.max_freq_stck = dict()
        

    def push(self, val: int) -> None:
        self.cnt[val] = self.cnt.get(val,0) + 1
        if self.cnt[val] > self.maxCnt:
            self.maxCnt = self.cnt[val]
        if self.cnt[val] not in self.max_freq_stck:
            self.max_freq_stck[self.cnt[val]] = [val]
        else:
            self.max_freq_stck[self.cnt[val]].append(val)

        

    def pop(self) -> int:
        val = self.max_freq_stck[self.maxCnt].pop()
        self.cnt[val] -= 1 
        if not self.max_freq_stck[self.maxCnt]:
            self.maxCnt -= 1
        return val

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()