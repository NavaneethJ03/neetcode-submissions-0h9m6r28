class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        hmap = {}
        for i , c in enumerate(s):
            hmap[c] = i
        l = 0
        farthest = 0
        for r , c in enumerate(s):
            farthest = max(farthest , hmap[c])
            if r == farthest:
                res.append(r - l + 1)
                l = r + 1
                farthest = 0 

        return res
            


