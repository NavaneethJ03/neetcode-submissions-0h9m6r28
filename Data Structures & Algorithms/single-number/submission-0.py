class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 
        for num in nums:
            print(num)
            print(res)
            res = res ^ num
            print(res)
        return res 