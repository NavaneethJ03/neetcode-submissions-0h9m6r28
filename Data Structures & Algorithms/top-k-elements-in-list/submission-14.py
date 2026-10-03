class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        bucket = [[] for _ in range(len(nums) + 1)]

        count = Counter(nums)

        for key , frq in count.items():
            bucket[frq].append(key)

        for i in range(len(bucket) - 1 , -1 , -1):
            for val in bucket[i]:
                res.append(val)
                k -= 1 
                if k == 0:
                    return res

        return res