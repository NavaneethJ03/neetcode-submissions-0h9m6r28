class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i , curSum):
            if i == len(nums):
                if curSum == target:
                    return 1
                return 0 

            key = (i , curSum)
            if key in memo:
                return memo[key]
            
            memo[key] = dfs(i + 1 , curSum + nums[i]) + dfs(i + 1 , curSum - nums[i])
            return memo[key]
        return dfs(0 , 0)