class TimeMap:

    def __init__(self):
        self.timeStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeStore:
            self.timeStore[key] = []
        self.timeStore[key].append([value , timestamp])

    def get(self, key: str, timestamp: int) -> str:

        values = self.timeStore.get(key , [])
        res = ""
        l , r = 0 , len(values) - 1
        while l <= r:
            m = (l + r) // 2 
            if values[m][1] == timestamp:
                return values[m][0]
            elif values[m][1] > timestamp:
                r = m - 1 
            else:
                res = values[m][0]
                l = m + 1

        return res
