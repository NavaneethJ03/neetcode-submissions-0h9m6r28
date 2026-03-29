class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin , currMax = 1 , 1

        for num in nums:
            temp = currMax * num 

            currMax = max(currMax * num , currMin * num , num)
            # if the num is positive , if num is negative , else prev num == 0
            currMin = min(currMin * num , temp , num)

            res = max(res , currMax)

        return res 
