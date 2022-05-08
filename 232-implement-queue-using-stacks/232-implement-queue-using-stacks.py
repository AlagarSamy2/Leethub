class MyQueue:

    def __init__(self):
        self.stacks=[]

    def push(self, x: int) -> None:
        self.stacks.append(x)
        

    def pop(self) -> int:
        return self.stacks.pop(0)

    def peek(self) -> int:
        return self.stacks[0]

    def empty(self) -> bool:
        return len(self.stacks)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()