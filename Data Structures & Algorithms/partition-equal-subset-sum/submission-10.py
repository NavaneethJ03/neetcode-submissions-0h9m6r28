class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False 

        dp = set([0])
        target = sum(nums) // 2
        for num in nums:
            nextDp = set()
            for t in dp:
                if t + num == target:
                    return True

                nextDp.add(t)
                nextDp.add(num + t)

            dp = nextDp

        return False 