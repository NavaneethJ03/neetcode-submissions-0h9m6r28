class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        if not self.stk:
            self.stk = [[val , val]]
        else:
            prev = self.stk[-1][1]
            self.stk.append([val , min(prev , val)])
        

    def pop(self) -> None:
        self.stk.pop()
        

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]
        
