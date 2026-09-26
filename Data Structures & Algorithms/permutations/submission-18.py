class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for num in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    copy = p.copy()
                    copy.insert(i , num)
                    new_perms.append(copy)

            perms = new_perms

        return perms