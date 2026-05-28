class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hset = {'+' , '-' , '*' , '/'}
        stk = []
        for t in tokens:
            if t not in hset:
                stk.append(int(t))
            else:
                b = int(stk.pop())
                a = int(stk.pop())
                if t == '+':
                    stk.append(a + b)
                elif t == '-':
                    stk.append(a - b)
                elif t == '*':
                    stk.append(a * b)
                else:
                    stk.append(int(float(a) / b))

        return stk[0]