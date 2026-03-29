class Solution:
    def isValid(self, s: str) -> bool:
        hset = {'}':'{',']':'[',')':'('}
        stk = []
        for c in s:
            if stk and c in hset:
                b = stk.pop()
                if b != hset[c]:
                    return False
            else:
                stk.append(c)

        return False if stk else True
