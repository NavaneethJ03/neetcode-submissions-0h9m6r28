class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        sub = []

        def dfs(i , curSum):
            if curSum == target:
                res.append(sub.copy())
                return 

            if curSum > target or i == len(candidates):
                return 

            sub.append(candidates[i])
            dfs(i + 1 , curSum + candidates[i])
            sub.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1 
            dfs(i + 1 , curSum)

        dfs(0 , 0)

        return res