class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for num in nums:
            new = []
            for p in perms:
                for i in range(len(p) + 1):
                    copy = p[:]
                    copy.insert(i , num)
                    new.append(copy)

            perms = new

        return perms 