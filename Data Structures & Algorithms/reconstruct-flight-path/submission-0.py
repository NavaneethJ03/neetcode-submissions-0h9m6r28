class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src , dst in sorted(tickets , reverse = True):
            graph[src].append(dst)

        stk = ["JFK"]
        res = []

        while stk:
            curr = stk[-1]
            if not graph[curr]:
                res.append(stk.pop())
            else:
                stk.append(graph[curr].pop())

        return res[::-1]