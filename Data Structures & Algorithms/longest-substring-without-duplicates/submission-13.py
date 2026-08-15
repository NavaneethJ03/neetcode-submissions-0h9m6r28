class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hset = set()
        l , r = 0 , 0
        ans = 0
        while r < len(s):
            while s[r] in hset:
                hset.remove(s[l])
                l += 1 
            hset.add(s[r])
            ans = max(ans , r - l + 1)
            r += 1 
        return ans