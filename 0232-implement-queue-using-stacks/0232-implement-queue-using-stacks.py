class MyQueue:

    def __init__(self):
        self.in_stackk = []
        self.out_stackk = []

    def push(self, x: int) -> None:
        self.in_stackk.append(x)
        return None
        

    def pop(self) -> int:
        self.peek()
        return self.out_stackk.pop()


    def peek(self) -> int:
        if not self.out_stackk:
            while self.in_stackk:
                val = self.in_stackk.pop()
                self.out_stackk.append(val)
        return self.out_stackk[-1]

    def empty(self) -> bool:
        if not self.in_stackk and not self.out_stackk:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()