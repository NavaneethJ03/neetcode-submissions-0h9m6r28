class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = set(nums)
        if len(n) != len(nums):
            return True
        else:
            return False