class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i , n in enumerate(nums):
            idx = abs(n) - 1 
            if nums[idx] < 0:
                return idx + 1 
            else:
                nums[idx] *= -1

