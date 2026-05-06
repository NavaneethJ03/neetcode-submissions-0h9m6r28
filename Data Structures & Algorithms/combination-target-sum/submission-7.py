class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []

        def dfs(i , curSum):
            if curSum == target:
                res.append(sub.copy())
                return 

            if i >= len(nums) or curSum > target:
                return 

            sub.append(nums[i])
            dfs(i, curSum + nums[i])
            sub.pop()
            dfs(i+1 , curSum)

        dfs(0 , 0)

        return res