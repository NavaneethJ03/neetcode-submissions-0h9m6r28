class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p , s] for p , s in zip(position , speed)]

        stk = []

        cars.sort(key = lambda x:x[0] , reverse = True)

        for p , s in cars:
            t = (target - p) / s
            if stk and t <= stk[-1]:
                continue 

            else:
                stk.append(t)

        return len(stk)