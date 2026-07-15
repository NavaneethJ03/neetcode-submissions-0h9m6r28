class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            new = []
            for p in perms:
                for i in range(len(p) + 1):
                    c = p.copy()
                    c.insert(i , n)
                    new.append(c)
            perms = new

        return perms