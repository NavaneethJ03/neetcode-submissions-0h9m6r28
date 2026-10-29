class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res 

    def decode(self, s: str) -> List[str]:
        l = r = 0 
        res = []
        while r < len(s) - 1:
            while s[r] != '#':
                r += 1 

            digit = int(s[l : r])
            l = r + 1 
            res.append(s[l : l + digit])
            r = l + digit
            l = r 

        return res

