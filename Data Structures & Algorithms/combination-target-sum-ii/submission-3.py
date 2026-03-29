class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        sub = []

        def dfs(i , curr):
            if curr == target:
                res.append(sub.copy())
                return 

            if i >= len(candidates) or curr > target:
                return 

            sub.append(candidates[i])
            dfs(i+1 , curr + candidates[i])
            sub.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1 

            dfs(i+1, curr)

        dfs(0 , 0)
        return res 
