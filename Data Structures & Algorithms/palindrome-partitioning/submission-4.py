class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []

        def backtrack(i):
            if i >= len(s):
                res.append(partition.copy())
                return 

            for j in range(i , len(s)):
                if self.isPalindrome(i , j , s):
                    partition.append(s[i:j+1])
                    backtrack(j + 1)
                    partition.pop()

        backtrack(0)  
        return res 

    def isPalindrome(self , l , r , s):
        while l < r:
            if s[l] != s[r]:
                return False 

            l += 1 
            r -= 1 

        return True

    