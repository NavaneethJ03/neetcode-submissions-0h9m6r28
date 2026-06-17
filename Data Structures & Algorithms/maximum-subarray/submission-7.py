class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub , maxCur = nums[0], 0


        for num in nums:
            if maxCur < 0:
                maxCur = 0 

            maxCur += num 
            maxSub = max(maxSub , maxCur)


        return maxSub