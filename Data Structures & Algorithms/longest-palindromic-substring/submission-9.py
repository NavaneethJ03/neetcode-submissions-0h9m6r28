class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0 
        res = [-1 , -1]

        def pali(l , r):
            nonlocal resLen , res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 >= resLen:
                    resLen = r - l + 1
                    res = [l , r]
                l -= 1 
                r += 1 

        for i in range(len(s)):
            pali(i , i)
            pali(i , i + 1)
        l , r = res
        return s[l : r+1] if resLen != 0 else ""            