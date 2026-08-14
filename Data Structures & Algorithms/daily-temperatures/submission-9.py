class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = []
        for i , t in enumerate(temperatures):
            while stk and t > stk[-1][1]:
                idx , temp = stk.pop()
                res[idx] = i - idx
            stk.append([i , t])

        return res