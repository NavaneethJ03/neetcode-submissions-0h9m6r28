class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = [-1 , -1]
        self.resLen = float('-inf')

        def pali(l , r , s):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if self.resLen <= (r - l + 1):
                    self.resLen = r - l + 1
                    self.res = [l , r]
                l -= 1 
                r += 1 

        for i in range(len(s)):
            pali(i , i , s)
            pali(i , i + 1 , s)

        l , r = self.res

        return s[l : r + 1]