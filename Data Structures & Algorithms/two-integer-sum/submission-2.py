class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i in range(len(nums)):
            hashset[nums[i]] = i 

        for i in range(len(nums)):
            if target - nums[i] in hashset and hashset[target - nums[i]] != i:
                return [i , hashset[target - nums[i]]]
            