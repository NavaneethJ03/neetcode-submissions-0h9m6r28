class Solution:
    def isValid(self, s: str) -> bool:
        hashmap =  { ')':'(','}':'{',']':'['}
        stk =[]
        for c in s:
            if c not in hashmap:
                stk.append(c)
            else:
                if not stk:
                    return False
                popped =  stk.pop()
                if popped != hashmap[c]:
                    return False

        return not stk
                    

        