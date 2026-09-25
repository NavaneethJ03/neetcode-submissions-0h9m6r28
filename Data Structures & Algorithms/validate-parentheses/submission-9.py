class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hset = {')':'(' , '}':'{' , ']':'['}

        for c in s:
            if c not in hset:
                stk.append(c)
            else:
                if not stk:
                    return False 
                if stk.pop() != hset[c]:
                    return False 

        return not stk