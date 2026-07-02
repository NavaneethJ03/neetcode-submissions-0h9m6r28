class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0 
        hset = set()
        l , r = 0 , 0 

        while r < len(s):
            while s[r] in hset:
                hset.remove(s[l])
                l += 1
            hset.add(s[r])
            ans = max(r - l + 1 , ans)
            r += 1 

        return ans 
                  
