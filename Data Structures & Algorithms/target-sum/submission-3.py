class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i , curSum):
            if i == len(nums):
                return 0 if target != curSum else 1
            key = (i , curSum)

            if key in memo:
                return memo[key]
            # there are only two operations to be performed add or sub

            memo[key] = dfs(i + 1 , curSum + nums[i]) + dfs(i + 1 , curSum - nums[i])

            return memo[key]
        return dfs(0 , 0)
            

