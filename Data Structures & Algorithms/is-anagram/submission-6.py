class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        chrMap = [0] * 26
        tMap = [0] * 26

        for i in range(len(s)):
            chrMap[ord(s[i]) - ord('a')] += 1 
            tMap[ord(t[i]) - ord('a')] += 1 

        return chrMap == tMap
