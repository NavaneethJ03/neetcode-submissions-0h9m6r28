class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        bucket = [[] for i in range(len(nums)+1)]
        for num , v in c.items():
            bucket[v].append(num)

        res = []
        
        for i in range(len(bucket) - 1, 0 , -1):
            for ele in bucket[i]:
                res.append(ele)
                if len(res) == k:
                    return res 


        

        