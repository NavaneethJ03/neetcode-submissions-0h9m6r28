class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s

        return res
        # 5#Hello5#World
    def decode(self, s: str) -> List[str]:
        res = []
        l = r = 0 
        while r < len(s) - 1:
            while s[r] != '#':
                r += 1
            
            length = int(s[l:r])
            l = r + 1 
            res.append(s[l : l + length])
            l = l + length 
            r = l 
        return res 