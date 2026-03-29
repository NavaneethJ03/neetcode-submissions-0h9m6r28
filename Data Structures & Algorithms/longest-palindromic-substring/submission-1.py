class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [-1 , -1]
        resLen = 0
        for i in range(len(s)):
            l , r = i , i # for odd palindromes 
            while 0 <= l < len(s) and 0 <= r < len(s) and s[l] == s[r]:
                if resLen < (r - l + 1):
                    res = [l , r]
                    resLen = r - l + 1
                l -= 1 
                r += 1 
            l , r = i , i + 1 # for even palindromes 
            while 0 <= l < len(s) and 0 <= r < len(s) and s[l] == s[r]:
                if resLen < (r - l + 1):
                    res = [l , r]
                    resLen = r - l + 1

                l -= 1 
                r += 1

        l , r = res

        return s[l : r + 1]

        