class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        j = len(s1)
        s = {}
        for c in s1:
            s[ord(c)-ord('a')] = 1 + s.get(ord(c) - ord('a'),0)

        for i in range(len(s2)-j+1):
            h = {}
            window = s2[i:i+j]
            print(window)
            for c in window:
                h[ord(c)-ord('a')] = 1 + h.get(ord(c)-ord('a'),0)
            if h == s:
                return True 

        return False 

