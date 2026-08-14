class Solution:
    def checkValidString(self, s: str) -> bool:
        stk = []
        star = []

        for i , c in enumerate(s):
            if c == '(':
                stk.append(i)

            elif c == '*':
                star.append(i)
            
            elif c == ')':
                if stk:
                    stk.pop()
                elif star:
                    star.pop()
                else:
                    return False 

        while stk:
            if not star:
                return False 

            a , b = stk.pop() , star.pop()
            if a > b:
                return False 

        return True