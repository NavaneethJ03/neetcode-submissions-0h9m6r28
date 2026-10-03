class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0 
        hset = set(nums)

        for n in hset:
            if n - 1 not in hset:
                length = 1 
                while n + length in hset:
                    length += 1 
                ans = max(ans , length)


        return ans