class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        sub = []

        def dfs(i , curSum):
            if curSum == target:
                res.append(sub[:])
                return 

            if i >= len(nums) or curSum > target:
                return 

            sub.append(nums[i])
            dfs(i + 1 , curSum + nums[i])
            sub.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1 
            dfs(i + 1 , curSum)

        dfs(0 , 0)
        return res