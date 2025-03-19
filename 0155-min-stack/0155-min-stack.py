class MinStack:

    def __init__(self):
        self.minStack = []
        self.normalStack = []
        self.minValue = 0

    def push(self, val: int) -> None:
        if len(self.normalStack) == 0:
            self.minValue = val
        else:
            self.minValue = min(self.minValue,val)
        
        self.normalStack.append(val)
        self.minStack.append(self.minValue)
    
    def pop(self) -> None:
        if len(self.normalStack) != 0 and len(self.minStack) != 0:
            self.normalStack.pop()
            self.minStack.pop()
            if len(self.minStack) != 0:
                self.minValue = self.minStack[-1]

    def top(self) -> int: 
        if len(self.normalStack) != 0:
            return self.normalStack[-1]
    
    def getMin(self) -> int:
        if len(self.minStack) != 0:
           
            return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()