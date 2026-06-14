class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.resLen =  -1 
        self.res = [-1 , -1]

        def helper(l , r , s):
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if r - l + 1 > self.resLen:
                        self.resLen = r - l + 1
                        self.res = [l , r]
                    l -= 1 
                    r += 1 
                else:
                    break

            return 

        for i in range(len(s)):
            helper(i , i , s)
            helper(i , i + 1 , s)
        
        l , r = self.res 
        return s[l : r + 1]

    