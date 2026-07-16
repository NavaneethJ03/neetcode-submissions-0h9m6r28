class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p , s] for p , s in zip(position , speed)]
        cars.sort(key = lambda x : x[0] , reverse = True)
        stk = []
        for p , s in cars:
            time = (target - p) / s
            if stk:
                if stk[-1] < time:
                    stk.append(time)

            else:
                stk.append(time)

        return len(stk)