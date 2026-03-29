class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        if not nums:
            return 0 
        ans = 1 
        for num in hset:
            if num - 1 not in hset:
                length = 1 
                while num + length in hset:
                    length += 1 
                    ans = max(ans , length)

        return ans 
