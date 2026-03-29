class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # we sort the nums 
        n = len(nums) 
        for i , a in enumerate(nums):
            if a > 0: # if the first itself is greater than zero , then no possibility 
                break 
            if i > 0 and a == nums[i - 1]: # skip duplicates 
                continue

            left , right = i + 1 , n - 1 
            while left < right:
                cur = a + nums[left] + nums[right]
                if cur == 0:
                    res.append([a , nums[left] , nums[right]])
                    left += 1 
                    right -= 1
                    while left < right and nums[left] == nums[left-1]: # skip duplicates 
                        left += 1 

                elif cur > 0:
                    right -= 1 

                else:
                    left += 1 

        return res 

