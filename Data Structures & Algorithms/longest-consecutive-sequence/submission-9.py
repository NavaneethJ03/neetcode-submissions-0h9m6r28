class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        ans = 0

        for num in nums:
            if num - 1 not in hset:
                length = 1 
                while num + length in hset:
                    length += 1 

                ans = max(ans , length)

        return ans 
