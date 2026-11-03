class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2:
            return False 
        dp = set()
        dp.add(0)

        target = sum(nums) // 2 

        for n in nums:
            next_dp = set()
            for t in dp:
                if n + t == target:
                    return True 
                next_dp.add(n + t)
                next_dp.add(t)

            dp = next_dp
        return False 