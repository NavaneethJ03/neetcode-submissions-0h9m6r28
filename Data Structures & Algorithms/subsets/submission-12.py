class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return 

            subset.append(nums[i]) # we pick
            backtrack(i + 1)
            subset.pop() # return to original state 
            backtrack(i + 1) # we skip 

        backtrack(0)
        return res 