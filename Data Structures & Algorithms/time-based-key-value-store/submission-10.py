class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([timestamp , value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.timeMap[key]
        if len(values) == 0:
            return ""

        l , r = 0 , len(values) - 1 

        ans = ""
        while l <= r:
            m = (l + r) // 2 
            if values[m][0] == timestamp:
                return values[m][1]
            elif values[m][0] > timestamp:
                r = m - 1 
            else:
                ans = values[m][1]
                l = m + 1

        return ans


