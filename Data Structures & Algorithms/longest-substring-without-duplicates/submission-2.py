class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        ans = 0 
        l = 0 
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1 
            charset.add(s[r])
            ans = max(ans,len(charset))

        return ans 
