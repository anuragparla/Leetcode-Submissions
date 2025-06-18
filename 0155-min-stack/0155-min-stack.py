'''
1) push()
Time complexity: O(1)
Space complexity: O(1)

2) pop()
Time complexity: O(1)
Space complexity: O(1)

3) top()
Time complexity: O(1)
Space complexity: O(1)

4) getMin()
Time complexity: O(1)
Space complexity: O(1)
'''
class MinStack:

    def __init__(self):
        self.minStack = []
        self.minValue = float('inf')

    def push(self, val: int) -> None:
        if val<=self.minValue:
            self.minStack.append(self.minValue)
            self.minValue = min(self.minValue,val)
            self.minStack.append(val)
        else:
            self.minStack.append(val)
    
    def pop(self) -> None:
            popped = self.minStack.pop()
            if popped == self.minValue:
                self.minValue = self.minStack.pop()

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