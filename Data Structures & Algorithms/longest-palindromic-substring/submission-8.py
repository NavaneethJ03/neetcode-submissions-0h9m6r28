class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.resLen = 0
        self.resIdx = 0
        def helper(s , l , r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if self.resLen <= r - l + 1:
                    self.resLen = r - l + 1 
                    self.resIdx = l 
                l -= 1 
                r += 1 

        for i in range(len(s)):
            helper(s , i , i + 1)
            helper(s , i , i)

        return s[self.resIdx:self.resIdx + self.resLen]
