class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)

        ans = 0 
        for n in nums:
            if n - 1 in hset:
                continue 

            else:
                length = 1 
                while n + length in hset:
                    length += 1 

                ans = max(ans , length)

        return ans 
