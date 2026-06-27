from collections import deque
class MyStack:

    def __init__(self):
        self.stck = deque([])
        

    def push(self, x: int) -> None:
        self.stck.append(x)
        

    def pop(self) -> int:
        if not self.empty():
            return self.stck.pop()
        return -1

        

    def top(self) -> int:
        if not self.empty():
            return self.stck[-1]
        return -1
        

    def empty(self) -> bool:
        if len(self.stck) == 0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()