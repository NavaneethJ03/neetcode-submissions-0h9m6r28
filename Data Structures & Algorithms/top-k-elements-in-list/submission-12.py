class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        ans = []
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num , 0)

        for key , cnt in count.items():
            bucket[cnt].append(key)

        for i in range(len(bucket) -1 , -1, -1):
            for ele in bucket[i]:
                ans.append(ele)
                k -= 1 
                if k == 0:
                    return ans