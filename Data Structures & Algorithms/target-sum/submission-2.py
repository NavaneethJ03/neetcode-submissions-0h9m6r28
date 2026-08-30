class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1 
        for i in range(len(nums)):
            nextDp = defaultdict(int)
            for curSum , count in dp.items():
                nextDp[curSum + nums[i]] += count
                nextDp[curSum - nums[i]] += count

            dp = nextDp

        return dp[target]
        # dp = {}

        # def backtrack(i , curSum):
        #     if i == len(nums):
        #         return 1 if curSum == target else 0 

        #     if (i , curSum) in dp:
        #         return dp[(i , curSum)]

        #     dp[(i , curSum)] = (backtrack(i + 1 , curSum + nums[i]) + backtrack(i + 1 , curSum - nums[i]))

        #     return dp[(i , curSum)]

        # return backtrack(0 , 0)