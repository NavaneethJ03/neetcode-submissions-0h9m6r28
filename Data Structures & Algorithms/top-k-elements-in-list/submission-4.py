class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # ans = []
        # d = {}
        # for i in range(len(nums)):
        #         d[nums[i]] = 1 + d.get(nums[i],0)
        #         d1 = sorted(d.items() , key = lambda item: item[1] , reverse = True )
        # for i in range(k):
        #     ans.append(d1[i][0])
        # return ans 
        # Own Brute force answer 

        # Optimal Bucket Sort 

        count = {}
        frq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)

        for n,c in count.items():
            frq[c].append(n)

        ans = []

        for i in range(len(frq)-1,0,-1):
            for n in frq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans 