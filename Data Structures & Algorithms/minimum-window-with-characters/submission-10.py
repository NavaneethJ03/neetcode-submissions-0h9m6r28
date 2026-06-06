class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        window_t = {}
        window_s = {}

        resLen = float("inf")
        res = [-1 , -1]

        for c in t:
            window_t[c] = 1 + window_t.get(c , 0)

        need = len(window_t)
        have = 0 
        l = 0 
        for r , c in enumerate(s):
            window_s[c] = 1 + window_s.get(c , 0)
            if c in window_t and window_s[c] == window_t[c]:
                have += 1 

            while have == need:
                if  (r - l + 1) < resLen:
                    resLen = (r - l + 1)
                    res = [l , r]

                window_s[s[l]] -= 1 

                if s[l] in window_t and window_s[s[l]] < window_t[s[l]]:
                    have -= 1 

                l += 1 



        l , r = res
        return s[l:r+1] if resLen != float("inf") else ""


