class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pre = 1
        pos = 1 
        for i , n in enumerate(nums):
            res[i] *= pre
            pre *= n

        for i in range(len(nums) - 1 , -1 , -1):
            res[i] *= pos
            pos *= nums[i]

        return res