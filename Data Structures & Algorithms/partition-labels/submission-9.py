class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        lastIdx = {}
        for i , c in enumerate(s):
            lastIdx[c] = i

        l = 0 
        seen = 0
        for r , c in enumerate(s):
            seen = max(seen , lastIdx[c])
            if seen == r:
                res.append(r - l + 1)
                l = r + 1 
            
        return res
