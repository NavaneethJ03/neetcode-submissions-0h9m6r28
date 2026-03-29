class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False 

        target = sum(nums) // 2

        dp = set()
        dp.add(0) # for base case 

        for i in range(len(nums) - 1 , -1 , -1):
            nextDp = set()
            for t in dp:
                if nums[i] + t == target:
                    return True
                nextDp.add(nums[i] + t)
                nextDp.add(t)
            dp = nextDp

        return False 