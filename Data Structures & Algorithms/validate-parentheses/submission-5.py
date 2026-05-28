class Solution:
    def isValid(self, s: str) -> bool:
        hset = {')':'(' , ']':'[' , '}':'{'}
        stk = []

        for c in s:
            if stk and c in hset:
                val = stk.pop()
                if val != hset[c]:
                    return False
            else:
                stk.append(c)

            
        return not stk 