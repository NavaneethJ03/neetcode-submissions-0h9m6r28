class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        candidates.sort()

        def dfs(i , cur):
            if cur == target:
                res.append(sub.copy())
                return 

            if i >= len(candidates) or cur > target:
                return 

            sub.append(candidates[i])
            dfs(i + 1 , cur + candidates[i])
            sub.pop()

            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1 
            dfs(i + 1 , cur)

        dfs(0 , 0)
        return res