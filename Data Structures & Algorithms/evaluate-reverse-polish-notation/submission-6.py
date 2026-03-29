class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        h = {'+' , '-' , '*' , '/'}
        for token in tokens:
            if token in h:
                n2 = stk.pop()
                n1 = stk.pop()
                if token == '+':
                    stk.append(n1 + n2)
                elif token == '-':
                    stk.append(n1 - n2)
                elif token == '*':
                    stk.append(n1 * n2)
                else:
                    stk.append(int(n1 / n2))

            else:
                stk.append(int(token))

        return stk[-1]