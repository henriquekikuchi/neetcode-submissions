class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_value = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, min_value))

    def pop(self) -> None:
        self.stack.pop() if self.stack else None
        
    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None
        
    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None
