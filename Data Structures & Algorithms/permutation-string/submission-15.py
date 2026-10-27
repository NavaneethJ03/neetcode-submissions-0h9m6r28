class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26

        for c in s1:
            count1[ord(c) - ord('a')] += 1 

        l = 0 
        for r , c in enumerate(s2):
            count2[ord(c) - ord('a')] += 1 
            if r - l + 1 == len(s1):
                if count1 == count2:
                    return True
                count2[ord(s2[l]) - ord('a')] -= 1 
                l += 1 
        return False 