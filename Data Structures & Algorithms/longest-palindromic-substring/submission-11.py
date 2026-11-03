class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0 
        res = [-1 , -1]

        def pali(l , r , s):
            nonlocal resLen , res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen <= r - l + 1:
                    resLen = r - l + 1 
                    res = [l , r]
                l -= 1 
                r += 1 
            

            
        for i in range(len(s)):
            pali(i , i , s) # for odd palindromes
            pali(i , i + 1 , s) # for even palindromes 

        l , r = res 

        return s[l : r + 1]



    