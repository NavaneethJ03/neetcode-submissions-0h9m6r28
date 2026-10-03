class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chrMap = [0] * 26
        target = [0] * 26

        for c in s:
            chrMap[ord(c) - ord('a')] += 1
        
        for c in t:
            target[ord(c) - ord('a')] += 1 

        if chrMap == target:
            return True
        return False 