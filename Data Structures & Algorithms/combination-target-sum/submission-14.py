class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i , curSum):
            if curSum == target:
                res.append(subset.copy())
                return 

            if curSum > target or i == len(nums):
                return 
            
            subset.append(nums[i])
            dfs(i , curSum + nums[i])
            subset.pop()
            dfs(i + 1 , curSum)

        dfs(0 , 0)
        return res 


        