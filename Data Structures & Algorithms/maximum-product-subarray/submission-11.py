class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = 1 
        ans = max(nums)

        for n in nums:
            temp = curMax * n
            curMax = max(curMax * n , curMin * n , n)
            curMin = min(curMin * n , temp , n)
            ans = max(ans , curMax)


        return ans