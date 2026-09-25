class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        minval = val
        if self.stk:
            minval = min(minval ,self.stk[-1][1])
        self.stk.append([val , minval])
            

    def pop(self) -> None:
        if self.stk:
            self.stk.pop()

    def top(self) -> int:
        if self.stk:
            return self.stk[-1][0]
        return -1

    def getMin(self) -> int:
        if self.stk:
            return self.stk[-1][1]
        return -1
        
