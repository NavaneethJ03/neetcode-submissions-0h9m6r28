class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        bucket = [[] for i in range(len(nums) + 1)]
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n , 0)
        for val , frq in count.items():
            bucket[frq].append(val)

        for i in range(len(bucket) - 1 , -1 , -1):
            for val in bucket[i]:
                res.append(val)
                k -= 1 
                if k == 0:
                    return res

        return res # this is for the edges where the expected k value is greater than the required one , just for safe case