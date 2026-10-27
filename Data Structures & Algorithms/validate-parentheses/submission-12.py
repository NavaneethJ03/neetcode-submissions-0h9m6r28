class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {')' : '(' , '}' : '{' , ']' : '['}
        stk = []

        for c in s:
            if c in hmap:
                if not stk or stk.pop() != hmap[c]:
                    return False 
            else:
                stk.append(c)

        return not stk