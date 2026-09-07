class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        curMax = 1
        curMin = 1

        for num in nums:
            temp = curMax * num
            curMax = max(curMax * num , curMin * num , num)
            curMin = min(curMin * num , temp , num)

            ans = max(ans , curMax)

        return ans