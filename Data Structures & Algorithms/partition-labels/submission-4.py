class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        lastSeen = {}
        for i , c in enumerate(s):
            lastSeen[c] = i
        
        l , r = 0 , 0 
        
        while r < len(s):
            dist = lastSeen[s[r]]
            while r < dist:
                r += 1 
                dist = max(dist , lastSeen[s[r]])
            res.append(r - l + 1)
            l = r + 1 
            r += 1

        return res