class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)

        for i , t in enumerate(temperatures):
            while stk and stk[-1][1] < t:
                idx , temp = stk.pop()
                res[idx] = i - idx 

            stk.append([i , t])

        return res 