class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subs = []
        def backtrack(i , curr):
            if curr == target:
                res.append(subs.copy())
                return 

            if i >= len(nums) or curr > target:
                return 

            subs.append(nums[i])
            backtrack(i , curr + nums[i])
            subs.pop()
            backtrack(i + 1 , curr)

        backtrack(0 , 0)
        return res