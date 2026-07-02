class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False 

        charArrS1 = [0] * 26 
        charArrS2 = [0] * 26 
        
        for c in s1:
            charArrS1[ord(c) - ord('a')] += 1

        l = 0 
        for r in range(len(s2)):
            c = s2[r]
            charArrS2[ord(c) - ord('a')] += 1 
            if r >= len(s1):
                charArrS2[ord(s2[l]) - ord('a')] -= 1 
                l += 1 

            if charArrS2 == charArrS1:
                return True 

        return False 
            