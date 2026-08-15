class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        ans = 0 
        maxF = 0 
        l = 0
        for r , c in enumerate(s):
            count[c] = 1 + count.get(c , 0)
            maxF = max(maxF , count[c])

            while r - l + 1 - maxF > k:
                count[s[l]] -= 1 
                l += 1

            ans = max(ans , r - l + 1)

        return ans 