class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1 
        for i , n in enumerate(nums):
            res[i] *= prefix 
            prefix *= n

        postfix = 1 
        for i in range(len(res) - 1 , -1 , -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res 