class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []

        def backtrack(i , curSum):
            if curSum == target:
                res.append(sub.copy())
                return 

            if i >= len(nums) or curSum > target:
                return 

            sub.append(nums[i])
            backtrack(i , curSum + nums[i])
            sub.pop()
            backtrack(i + 1 , curSum)


        backtrack(0 , 0)

        return res 