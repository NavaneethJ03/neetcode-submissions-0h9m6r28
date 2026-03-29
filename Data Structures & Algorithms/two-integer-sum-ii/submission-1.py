class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers) - 1 

        while l < r :
            summ = numbers[l] + numbers[r]
            if summ == target:
                return [l + 1, r + 1]
            else:
                if target > summ:
                    l += 1
                else:
                    r -= 1 

