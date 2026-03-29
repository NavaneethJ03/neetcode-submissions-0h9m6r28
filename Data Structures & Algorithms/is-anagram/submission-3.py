class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 , s2 = {} , {}
        for c in s:
            s1[c] = 1 + s1.get(c , 0)

        for c in t:
            s2[c] = 1 + s2.get(c , 0)
        return s1 == s2

    