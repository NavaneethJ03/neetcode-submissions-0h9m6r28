class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        l = r = 0 
        while r < len(s):
            while s[r] != '#':
                r += 1 
            length = int(s[l:r])
            # shift l to r + 1 
            l = r + 1 
            res.append(s[l:l + length])
            r = l + length 
            l = r 
        return res