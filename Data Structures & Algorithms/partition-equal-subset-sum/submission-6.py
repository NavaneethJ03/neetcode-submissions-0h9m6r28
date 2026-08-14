class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False 

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for num in nums:
            nextDp = set()
            for d in dp:
                if num + d == target:
                    return True
                nextDp.add(num + d)
                nextDp.add(d)

            dp = nextDp
        
        return False 