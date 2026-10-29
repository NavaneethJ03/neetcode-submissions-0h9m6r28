class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chrMap = [0] * 26 
        for c in s:
            chrMap[ord(c) - ord('a')] += 1
        
        for c in t:
            chrMap[ord(c) - ord('a')] -= 1 

        for c in chrMap:
            if c != 0:
                return False 

        return True 