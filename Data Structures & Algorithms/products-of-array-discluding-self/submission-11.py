class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre = 1 

        for num in nums:
            res.append(pre)
            pre *= num 

        pos = 1 

        for i in range(len(nums) - 1 , -1 , -1):
            res[i] *= pos 
            pos *= nums[i]


        return res