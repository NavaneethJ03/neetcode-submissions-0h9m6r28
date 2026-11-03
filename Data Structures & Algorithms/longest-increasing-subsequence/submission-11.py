class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = 0 
        dp = [1] * len(nums)
        for i in range(len(nums) - 1 , -1 , -1):
            for j in range(i + 1 , len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i] , dp[j] + 1)


        return max(dp)