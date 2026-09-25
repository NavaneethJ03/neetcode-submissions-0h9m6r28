class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + '#' + word
        return res 
    def decode(self, s: str) -> List[str]:
        # 5#Hello5#World
        l , r = 0 , 0 
        res = []
        while r < len(s):
            while s[r] != '#':
                r += 1 
            length = int(s[l:r])
            l = r + 1 
            r = l + length
            res.append(s[l:r])
            l = r 

        return res
