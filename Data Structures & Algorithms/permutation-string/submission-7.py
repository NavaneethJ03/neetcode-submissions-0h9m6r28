class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        counter1 = [0] * 26 
        counter2 = [0] * 26
        for c in s1:
            counter1[ord(c) - ord('a')] += 1

        for i in range(len(s1)):
            counter2[ord(s2[i]) - ord('a')] += 1 

        if counter1 == counter2:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            counter2[ord(s2[l]) - ord('a')] -= 1 
            counter2[ord(s2[r]) - ord('a')] += 1 
            l += 1
            if counter1 == counter2:
                return True

        return False