class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxF = 0 
        count = {}
        res = 0 

        left = 0 

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r] , 0)
            maxF = max(maxF , count[s[r]])
            while (r - left + 1) - maxF > k:
                count[s[left]] -= 1 
                left += 1 

            res = max(res , r - left + 1)


        return res 