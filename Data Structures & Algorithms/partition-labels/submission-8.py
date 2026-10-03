class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        lastSeen = {}
        for i , c in enumerate(s):
            lastSeen[c] = i

        l = 0 
        far = 0
        for r , c in enumerate(s):
            far = max(far , lastSeen[c])
            if r == far:
                res.append(r - l + 1)
                l = r + 1 
            
        return res