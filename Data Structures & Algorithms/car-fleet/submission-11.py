class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        cars = [[p,s] for p , s in zip(position , speed)]
        cars.sort(key = lambda x : x[0] , reverse = True)

        for p , s in cars:
            time = (target - p) / s
            if stk and time <= stk[-1]:
                continue

            stk.append(time)


        return len(stk)
