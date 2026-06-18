class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # tried a new method called the reversed to implement easy code in reversing the for loops 
        # what we try to do is to shrink the goal from the last to the start if we reach the start then we return True
        n = len(nums)
        goal = len(nums) - 1 
        for i in reversed(range(n - 1)):
            jmp = nums[i]
            if i + jmp >= goal:
                goal = i

        return goal == 0