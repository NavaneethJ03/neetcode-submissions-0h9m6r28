class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = set(nums)
        ans = 1

        if not nums:
            return 0
        for num in h:
            if num - 1 not in h:
                length = 1 
                while num + length in h:
                    length += 1 
                    
                ans = max(ans , length)

        return ans 


        