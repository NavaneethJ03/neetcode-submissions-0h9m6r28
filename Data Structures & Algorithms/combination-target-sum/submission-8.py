class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i , curSum):

            if curSum == target:
                res.append(subset.copy())
                return 
            if i >= len(nums) or curSum > target:
                return

            subset.append(nums[i])
            backtrack(i, curSum + nums[i])
            subset.pop()
            backtrack(i + 1 , curSum)

        backtrack(0 , 0)

        return res 