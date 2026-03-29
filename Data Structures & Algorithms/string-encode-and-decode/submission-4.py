class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res


    def decode(self, s: str) -> List[str]:
        l = r = 0 
        output = []
        while r < len(s):
            if s[r] == "#":
                length = int(s[l:r])
                l = r + 1
                r = l + length
                output.append(s[l:r])
                l = r
            else:
                r += 1 
        return output
