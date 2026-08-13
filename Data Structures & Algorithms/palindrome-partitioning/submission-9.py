class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sub = []

        def backtrack(i):
            if i >= len(s):
                res.append(sub.copy())
                return 

            for j in range(i , len(s)):
                if self.isPali(s , i , j):
                    sub.append(s[i:j+1])
                    backtrack(j + 1)
                    sub.pop()
        backtrack(0)
        return res
    def isPali(self , s , i , j):
        while i < j:
            if s[i] == s[j]:
                i += 1 
                j -= 1 

            else:
                return False 

        return True 