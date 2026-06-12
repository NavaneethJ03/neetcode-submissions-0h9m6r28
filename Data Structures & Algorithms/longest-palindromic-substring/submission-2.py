class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        res = [-1 , -1]
        resLen = 0 

        for i in range(n):
            l , r = i , i 
            while 0 <= l < n and 0 <= r < n and s[l] == s[r]:
                if r - l + 1 >= resLen:
                    res = [l , r]
                    resLen = r - l + 1

                r += 1 
                l -= 1 
            l , r = i , i + 1 

            while 0 <= l < n and 0 <= r < n and s[l] == s[r]:
                if r - l + 1 >= resLen:
                    res = [l , r]
                    resLen = r - l + 1

                r += 1 
                l -= 1 


        l , r = res 

        return s[l : r + 1]

            