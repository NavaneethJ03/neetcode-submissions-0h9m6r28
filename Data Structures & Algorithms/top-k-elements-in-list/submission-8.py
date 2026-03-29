class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frq = [[] for _ in range(len(nums)+1)]
        for num in nums:
            count[num] = 1 + count.get(num , 0)

        for n , cnt in count.items():
            frq[cnt].append(n)

        res = []

        for i in range(len(frq) - 1 , -1 , -1):
            for num in frq[i]:
                res.append(num)
                if len(res) == k:
                    return res