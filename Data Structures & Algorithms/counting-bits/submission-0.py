class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)

        for i in range(n + 1):
            j = i 
            while j:
                j &= j - 1
                res[i] += 1

        return res 

         