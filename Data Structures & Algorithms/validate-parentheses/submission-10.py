class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hset = {')':'(' , '}':'{' , ']':'['}

        for c in s:
            if c in hset:
                if stk and stk.pop() == hset[c]:
                    continue
                else:
                    return False 

            else:
                stk.append(c)
        
        return not(stk)
                    