class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num , 0)

        for num , frq in count.items():
            bucket[frq].append(num)

        res = []

        for i in range(len(bucket) - 1 , - 1 , -1):
            for item in bucket[i]:
                res.append(item) 
                k -= 1 
                if k == 0:
                    return res 

        
