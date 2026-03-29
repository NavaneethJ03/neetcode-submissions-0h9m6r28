class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        # Brute Force Solution 
        # res = [0] * len(t)
        # i = 0 
        # while i < len(t):
        #     j = i
        #     while j < len(t):
        #         if t[j] > t[i]:
        #             res[i] = j - i
        #             break 
        #         j += 1  
        #     i += 1 
        # return res
        # using Monotonic Stack 
        res = [0] * len(temp)
        stk = []
        for i , t in enumerate(temp):
            while stk and t > stk[-1][0]:
                stktemp , stkindex = stk.pop()
                res[stkindex] = i - stkindex
            stk.append([t , i])
        return res 


        