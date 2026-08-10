class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word))
            res += "#"
            res += word

        return res
    def decode(self, s: str) -> List[str]:
        i = j = 0 
        res = []
        while j < len(s):
            while s[j] != '#':
                j += 1 

            length = int(s[i : j])
            i = j + 1 
            res.append(s[i : i + length])
            i += length
            j = i

        return res
