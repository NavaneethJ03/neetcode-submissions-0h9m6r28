class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = []

        for i ,t in enumerate(temperatures):
            if not stk:
                stk.append((t , i))
            else:
                while stk and t > stk[-1][0]:
                    temp , idx = stk.pop()
                    res[idx] = i - idx
                else:
                    stk.append((t , i))

        return res

            
        