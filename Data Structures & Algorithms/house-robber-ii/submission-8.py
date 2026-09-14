class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            if len(nums) == 2:
                return max(nums)
            
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0] , nums[1])
            for i in range(2 , len(nums)):
                dp[i] = max(dp[i - 1] , nums[i] + dp[i - 2])

            return dp[-1]

        if len(nums) <= 3:
            return max(nums)

        return max(helper(nums[0 : len(nums) - 1]) , helper(nums[1:]))