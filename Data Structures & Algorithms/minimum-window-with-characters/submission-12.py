from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = [-1 , -1]
        resLen = float('inf')
        if len(t) > len(s): # edge case check
            return ""

        countT = defaultdict(int)
        countS = defaultdict(int)

        for c in t:
            countT[c] += 1 
        l = 0 
        have , need  = 0 , len(countT)
        for r , c in enumerate(s):
            countS[c] += 1 
            if c in countT and countT[c] == countS[c]:
                have += 1 
            while have == need:
                if r - l + 1 < resLen:
                    res = [l , r]
                    resLen = r - l + 1 

                countS[s[l]] -= 1 
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1 

                l += 1 

        l , r = res 
        return s[l : r + 1] if resLen != float('inf') else ""
