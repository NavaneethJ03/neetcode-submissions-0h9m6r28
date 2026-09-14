class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0 
        # def isPali(s , l , r):
        #     while l < r:
        #         if s[l] != s[r]:
        #             return False 
        #         l += 1 
        #         r -= 1
        #     return True
        for i in range(len(s)):
            l , r = i , i  
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    self.count += 1 
                    l -= 1 
                    r += 1 
                else:
                    break
            l , r = i , i + 1 
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    self.count += 1 
                    l -= 1 
                    r += 1 
                else:
                    break
                    
        return self.count

