class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value , timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        res = ""
        vals = self.timeMap[key]
        l , r = 0 , len(vals) - 1 
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


