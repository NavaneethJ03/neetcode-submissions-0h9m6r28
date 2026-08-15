class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) >  len(s2):
            return False 

        t = [0] * 26
        s = [0] * 26
        for c in s1:
            t[ord(c) - ord('a')] += 1

        l = 0 
        for r , c in enumerate(s2):
            s[ord(c) - ord('a')] += 1
            if r - l + 1 == len(s1):
                if t == s:
                    return True
                s[ord(s2[l]) - ord('a')] -= 1 
                l += 1 
            

        return False 