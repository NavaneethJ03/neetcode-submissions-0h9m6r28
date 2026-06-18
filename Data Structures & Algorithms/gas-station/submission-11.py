class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1 
        total = 0
        res = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0 
                res = i + 1 

        return res 
        
        # tank = shortage = 0 

        # index = 0 

        # for i in range(len(gas)):
        #     tank += gas[i]
        #     if tank >= cost[i]:
        #         tank -= cost[i]
        #     else:
        #         shortage = cost[i] - tank
        #         index = i + 1 
        #         tank = 0 

        # if index == len(gas):
        #     return -1 

        # return index