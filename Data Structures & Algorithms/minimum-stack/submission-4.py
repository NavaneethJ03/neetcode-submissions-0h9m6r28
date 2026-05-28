class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        if self.stk:
            minn = min(self.stk[-1][1] , val)
            self.stk.append([val , minn])
        else:
            self.stk.append([val , val])

    def pop(self) -> None:
        if self.stk:
            return self.stk.pop()

    def top(self) -> int:
        if self.stk:
            return self.stk[-1][0]

    def getMin(self) -> int:
        if self.stk:
            return self.stk[-1][1]