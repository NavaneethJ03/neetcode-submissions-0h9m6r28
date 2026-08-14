class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for t in tokens:
            if t == '+':
                b = int(stk.pop())
                a = int(stk.pop())
                stk.append(a + b)
            elif t == '-':
                b = int(stk.pop())
                a = int(stk.pop())
                stk.append(a - b)
            elif t == '*':
                b = int(stk.pop())
                a = int(stk.pop())
                stk.append(a * b)
            elif t == '/':
                b = int(stk.pop())
                a = int(stk.pop())
                stk.append(int((a) / b))
            else:
                stk.append(int(t))

        return stk[0]