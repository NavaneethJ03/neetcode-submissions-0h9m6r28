class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False 

        target = sum(nums) // 2 
        dp = set([0])

        for num in nums:
            nextDp = set()
            for t in dp:
                if num + t == target:
                    return True

                nextDp.add(t)
                nextDp.add(num + t)

            dp = nextDp

        return False
