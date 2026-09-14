class Solution:
    def checkValidString(self, s: str) -> bool:
        star = []
        stk = []

        for i , c in enumerate(s):
            if c == '(':
                stk.append(i)
            elif c == '*':
                star.append(i)
            else:
                if stk:
                    stk.pop()
                elif star:
                    star.pop()
                else:
                    return False 

        while stk and star:
            if stk.pop() > star.pop():
                return False 

        return not stk