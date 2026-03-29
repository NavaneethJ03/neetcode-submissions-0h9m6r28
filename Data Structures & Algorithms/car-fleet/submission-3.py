class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p , s] for p , s in zip(position , speed)]
        cars.sort(key = lambda x : x[0] , reverse = True)
        stack = []

        for pos , speed in cars:
            time = (target - pos) / speed
            if stack and stack[-1] >= time:
                pass
            else:
                stack.append(time)
        return len(stack)
