class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = 0
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0] , nums[1])
        def helper(nums):
            if len(nums) == 0:
                return 0
            if len(nums) == 1:
                return nums[0]
            elif len(nums) == 2:
                return max(nums[0] , nums[1])
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0] , nums[1])

            for idx in range(2 , len(nums)):
                dp[idx] = max(dp[idx - 2] + nums[idx] , dp[idx - 1])

            return dp[-1]
        
        ans = max(helper(nums[0:-1]) , helper(nums[1:]))
        return ans
