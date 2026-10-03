class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0 
        for num in nums:
            print(xor)
            print(num)
            xor ^= num 
            print(xor)
        return xor