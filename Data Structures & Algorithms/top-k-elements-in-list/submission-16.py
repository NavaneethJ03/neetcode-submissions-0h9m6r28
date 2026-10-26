class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        bucket = [[] for _ in range(n + 1)]
        count = Counter(nums)
        for key , v in count.items():
            bucket[v].append(key)

        t = 0
        res = []
        for i in range(len(bucket) - 1 , -1 , -1):
            for b in bucket[i]:
                res.append(b)
                t += 1 
                if t == k:
                    return res 

        return res

