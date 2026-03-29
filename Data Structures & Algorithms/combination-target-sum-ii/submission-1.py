class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        candidates.sort()

        def backtrack(idx , curr):
            if curr == target:
                res.append(sub.copy())
                return

            for i in range(idx , len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if curr + candidates[i] > target:
                    break
      
                sub.append(candidates[i])
                backtrack(i+1 , curr + candidates[i])
                sub.pop()

    


        backtrack(0 , 0)
        return res