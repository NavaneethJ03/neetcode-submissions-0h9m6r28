class Solution:
    def isValid(self, s: str) -> bool:
        hset = {')':'(' , ']':'[' , '}':'{'}
        stk = []

        for c in s:
            if stk and c in hset:
                if hset[c] != stk.pop():
                    return False 

            else:
                stk.append(c)


        return not stk 
        