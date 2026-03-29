class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        # Brute Force Solution 
        res = [0] * len(t)
        i = 0 
        while i < len(t):
            j = i
            while j < len(t):
                if t[j] > t[i]:
                    res[i] = j - i
                    break 
                j += 1  
            i += 1 
        return res
