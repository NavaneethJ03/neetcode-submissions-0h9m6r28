class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        d = {}
        for i in range(len(nums)):
                d[nums[i]] = 1 + d.get(nums[i],0)
                d1 = sorted(d.items() , key = lambda item: item[1] , reverse = True )
                # d = dict(d1)
        for i in range(k):
            ans.append(d1[i][0])
        return ans 