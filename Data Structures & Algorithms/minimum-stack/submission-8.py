class MinStack:

    def __init__(self): 
        self.stk = []

    def push(self, val: int) -> None:
        min_val = val
        if self.stk:
            min_val = min(self.stk[-1][1] , val)
        self.stk.append([val , min_val])

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
