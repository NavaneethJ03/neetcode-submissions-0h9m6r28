class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = [-1 , -1]
        resLen = float('inf')

        count = Counter(t)
        need = len(count)
        have = 0 

        window = {}
        l = 0 

        for r , c in enumerate(s):
            window[c] = 1 + window.get(c , 0)
            if window[c] == count[c]:
                have += 1 
            while have == need:
                if r - l + 1 <= resLen:
                    resLen = r - l + 1
                    res = [l , r]
                
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1 
                l += 1 

        l , r = res 
        return s[l : r + 1] if l != -1 else ""



