class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == '':
            return ''

        resLen = float('inf')
        res = [-1 , -1]

        count = Counter(t)
        window = {}
        need = len(count)
        have = 0 
        l = 0 
        for r , c in enumerate(s):
            window[c] = 1 + window.get(c , 0)
            if c in count and count[c] == window[c]:
                have += 1 
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l , r]
                window[s[l]] -= 1 
                if s[l] in count and count[s[l]] > window[s[l]]:
                    have -= 1 
                l += 1 

        l , r = res 
        return s[l : r + 1] if resLen != float('inf') else ""