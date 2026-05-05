class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        count = {}
        window = {}
        res = [-1 , -1]
        resLen = float("inf")
        for c in t:
            count[c] = 1 + count.get(c , 0)
        have , need = 0 , len(count)
        l = 0
        for r in range(len(s)):
            ch = s[r]
            window[ch] = 1 + window.get(ch , 0)
            if ch in count and count[ch] == window[ch]:
                have += 1 
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l , r]
                    resLen = r - l + 1

                window[s[l]] -= 1 

                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1 

                l += 1 

        l , r = res 
        return s[l : r + 1] if resLen != float("inf") else ""