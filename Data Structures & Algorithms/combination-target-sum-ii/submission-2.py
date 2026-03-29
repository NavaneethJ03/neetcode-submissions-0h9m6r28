class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        candidates.sort()
        def dfs(i , cur):
            if cur == target:
                res.append(sub.copy())
                return 

            for idx in range(i , len(candidates)):
                if idx > i and candidates[idx] == candidates[idx - 1]:
                    continue 

                if cur + candidates[idx] > target:
                    break

                sub.append(candidates[idx])
                dfs(idx + 1 , cur + candidates[idx])
                sub.pop()



        dfs(0 , 0)
        return res

