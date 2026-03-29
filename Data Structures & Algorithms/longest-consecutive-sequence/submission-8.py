class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hset = set(nums)
        res = 1 
        for num in nums:
            if num - 1 not in hset:
                length = 1
                while num + length in hset:
                    length += 1 
                    res = max(res , length)
        return res 
