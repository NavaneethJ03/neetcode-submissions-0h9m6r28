class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position , speed)) , key = lambda x : x[0] , reverse = True)

        stk = []

        for p , s in cars:
            time = (target - p) / s
            if stk and stk[-1] >= time:
                continue
            else:
                stk.append(time)

        return len(stk)