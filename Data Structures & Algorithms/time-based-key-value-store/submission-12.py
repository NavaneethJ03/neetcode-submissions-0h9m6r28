class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value , timestamp])

    def get(self, key: str, timestamp: int) -> str:
        vals = self.store.get(key , [])
        res = ""
        l , r = 0 , len(vals) - 1 
        while l <= r:
            m = (l + r) // 2 
            if vals[m][1] == timestamp:
                return vals[m][0]
            elif vals[m][1] > timestamp:
                r = m - 1
            else:
                res = vals[m][0]
                l = m + 1 

        return res


        
