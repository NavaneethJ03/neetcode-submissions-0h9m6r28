class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0 
        l = r = 0
        h = set()
        while r < len(s):
            if s[r] not in h:
                h.add(s[r])
                r += 1 
            else:
                h.remove(s[l])
                l += 1 

            res = max(res , r - l)
                

        return res

        