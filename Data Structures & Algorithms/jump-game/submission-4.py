class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = len(nums) - 1 
        for i in reversed(range(n - 1)):
            jmp = nums[i]
            if i + jmp >= goal:
                goal = i

        return goal == 0