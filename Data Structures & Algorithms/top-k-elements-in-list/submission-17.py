class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        bucket = [[] for i in range(n + 1)]

        res = []
        count = Counter(nums)

        for key , v in count.items():
            bucket[v].append(key)

        for i in range(len(bucket) - 1 , -1 , -1):
            for b in bucket[i]:
                if k == 0:
                    return res 
                res.append(b)
                k -= 1 

        return res