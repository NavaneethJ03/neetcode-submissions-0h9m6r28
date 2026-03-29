class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        if not self.stk:
            self.stk.append((val , val))
        else:
            curr_min = self.stk[-1][1]
            self.stk.append((val ,min(curr_min , val)))

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]
