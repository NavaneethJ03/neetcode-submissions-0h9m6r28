class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        h = {')' : '(' , ']' : '[' , '}' : '{'}

        for c in s:
            if c not in h:
                stk.append(c)

            else:
                if stk:
                    t = stk.pop()
                    if t != h[c]:
                        return False 
                
                else:
                    return False 

            
        return not stk