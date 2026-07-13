from collections import defaultdict
class TimeMap:

    def __init__(self):
       self.store = defaultdict(list) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value , timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        vals = self.store.get(key , [])
        if not vals:
            return ""
        l , r = 0 , len(vals) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2 
            if vals[m][1] == timestamp:
                return vals[m][0]
            elif vals[m][1] < timestamp:
                res = vals[m][0]
                l = m + 1 
            else:
                r = m - 1 

        return res 

