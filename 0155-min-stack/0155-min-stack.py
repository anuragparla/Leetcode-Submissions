class MinStack:

    def __init__(self):
        self.minStack = []
        self.minValue = float('inf')

    def push(self, val: int) -> None:
        # when stack is empty, 1st value pushed is the min val
        if val<=self.minValue:
            self.minStack.append(self.minValue)
            self.minValue = min(self.minValue,val)
            self.minStack.append(val)
        else:
            self.minStack.append(val)
    
    def pop(self) -> None:
        # always check if stack is empty before popping
            popped = self.minStack.pop()
            if popped == self.minValue:
                self.minValue = self.minStack.pop()

        # after popping, make sure stack not empty before accessing
            # if len(self.minStack) != 0:
            #     self.minValue = self.minStack[-1]

    def top(self) -> int: 
        if len(self.minStack) > 0:
            return self.minStack[-1]
    
    def getMin(self) -> int:
        return self.minValue
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()