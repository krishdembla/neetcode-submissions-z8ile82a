class MyQueue:

    def __init__(self):
        self.s1 = [] #input stack
        self.s2 = [] #output stack

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2: #s2 is empty
            while self.s1:
                temp = self.s1.pop()
                self.s2.append(temp)
            return self.s2.pop()
        else:
            return self.s2.pop()

    def peek(self) -> int:
        if self.s2:
            return self.s2[-1]
        else:
            return self.s1[0]

    def empty(self) -> bool:
        if not self.s1 and not self.s2:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()