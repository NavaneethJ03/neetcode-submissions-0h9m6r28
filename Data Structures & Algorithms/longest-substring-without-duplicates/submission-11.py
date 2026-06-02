class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0 
        l = r = 0 
        n = len(s)
        hset = set()

        while r < n:
            if s[r] not in hset:
                hset.add(s[r]) 
                res = max(res , r - l + 1)
                r += 1 
            else:
                hset.remove(s[l])
                l += 1

        return res 
            