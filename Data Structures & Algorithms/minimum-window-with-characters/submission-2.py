class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''

        resLen = float('inf')
        res = [-1 , -1]
        countT = {}
        countS = {}
        for c in t:
            countT[c] = 1 + countT.get(c , 0)

        have , need = 0 , len(countT)
        l = 0
        for r in range(len(s)):
            c = s[r]
            countS[c] = 1 + countS.get(c , 0)
            if c in countT and countS[c] == countT[c]:
                have += 1 
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l , r]
                    resLen = (r - l + 1)
                countS[s[l]] -= 1 
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1 

                l += 1 

        l , r = res
        return s[l: r + 1] if resLen != float('inf') else ''

