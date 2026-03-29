class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        arr = [(start , end , end - start + 1) for start , end in intervals]
        arr.sort(key = lambda x : x[2])
        res = [-1] * len(queries)

        for i in range(len(queries)):
            for j in range(len(arr)):
                if queries[i] in range(arr[j][0] , arr[j][1] + 1):
                    res[i] = arr[j][2]
                    break 

        return res 