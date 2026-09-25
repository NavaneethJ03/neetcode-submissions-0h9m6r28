class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0 
        hset = set()
        for r , c in enumerate(s):
            while c in hset:
                hset.remove(s[l])
                l += 1 
            hset.add(c)
            ans = max(ans , r - l + 1)

        return ans