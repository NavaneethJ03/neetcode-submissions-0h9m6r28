class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        lastSeen = {}
        for i , c in enumerate(s):
            lastSeen[c] = i

        l = 0
        seen = 0
        for r , c in enumerate(s):
            seen = max(seen , lastSeen[c])
            if r == seen:
                res.append(r - l + 1)
                l = r + 1 
        return res
