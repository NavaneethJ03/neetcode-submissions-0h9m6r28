class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []

        def backtrack(i):
            if i >= len(nums):
                res.append(sub.copy())
                return 

            
            backtrack(i+1)
            sub.append(nums[i])
            backtrack(i+1)
            sub.pop()

        backtrack(0)

        return res 
