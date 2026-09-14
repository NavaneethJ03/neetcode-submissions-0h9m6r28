class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        lastSeen = {}
        for i , c in enumerate(s):
            lastSeen[c] = i
        
        l = 0 
        dist = 0 
        for r , c in enumerate(s):
            dist = max(dist , lastSeen[c])
            if r == dist:
                res.append(r - l + 1)
                l = r + 1 
                dist = 0 

        return res