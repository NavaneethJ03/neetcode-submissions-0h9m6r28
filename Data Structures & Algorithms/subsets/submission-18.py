class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # base case 
        # constraints 
        # recursive condition 
        # return 
        res = []
        subset = []
        def backtrack(i):
            # define base case 
            if i == len(nums):
                res.append(subset.copy())
                return 

            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res 

