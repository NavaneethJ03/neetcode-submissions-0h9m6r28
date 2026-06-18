class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res , cur =  nums[0], 0 # init the first value to res to avoid the neg no tests
        for num in nums:
            cur += num # update the cursum
            res = max(res , cur) # update the max 
            if cur < 0: # if the subarray leads to negative then ditch and start a new one 
                cur = 0 

        return res 