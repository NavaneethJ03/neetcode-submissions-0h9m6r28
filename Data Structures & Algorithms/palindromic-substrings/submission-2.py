class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0    
        for i in range(len(s)):
            self.isPali(i , i , s)
            self.isPali(i , i + 1 , s)

        return self.count
    def isPali(self , l , r , s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            self.count += 1 
            l -= 1 
            r += 1 