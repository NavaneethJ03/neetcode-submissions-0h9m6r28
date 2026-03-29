class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        candidates.sort()

        def backtrack(i , curSum):
            if curSum == target:
                res.append(sub.copy())
                return 

            if i >= len(candidates) or curSum > target:
                return 

            sub.append(candidates[i])
            backtrack(i + 1 , curSum + candidates[i])
            sub.pop()
            while (i + 1) < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1 

            backtrack(i + 1 , curSum)

        backtrack(0 , 0)

        return res 

