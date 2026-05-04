class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i in range(len(nums)):
            if target - nums[i] in prevMap:
                return [prevMap[target - nums[i]] , i]
            else:
                prevMap[nums[i]] = i

        