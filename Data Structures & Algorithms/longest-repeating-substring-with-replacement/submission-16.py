class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0 
        count = {}
        maxF = 0 
        l = 0 
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r] , 0)
            maxF = max(maxF , count[s[r]])

            if r - l + 1 - maxF > k:
                count[s[l]] -= 1 
                l += 1 

            ans = max(ans , r - l + 1)

        return ans 