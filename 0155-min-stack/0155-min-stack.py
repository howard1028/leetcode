class MinStack:

    def __init__(self):
        self.stack = [] # stack
        self.min_stack = [] # min stack

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.min_stack) == 0 or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if len(self.stack) != 0:
            if self.stack[-1] == self.min_stack[-1]: # 先check再pop stack
                self.min_stack.pop()

            self.stack.pop()

    def top(self) -> int:
        if len(self.stack) != 0:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.min_stack) != 0:
            return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()