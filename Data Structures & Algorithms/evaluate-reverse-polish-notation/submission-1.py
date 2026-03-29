class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        h = {'+','-','*','/'}
        for token in tokens:
            if token not in h:
                stk.append(token)

            else:
                b = int(stk.pop())
                a = int(stk.pop())
                if token == '+':
                    stk.append(a+b)
                elif token == '-':
                    stk.append(a-b)
                elif token == '*':
                    stk.append(a*b)
                else:
                    stk.append(int(float(a)/b))
        return int(stk[0])