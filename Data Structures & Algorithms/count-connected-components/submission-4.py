class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        graph = {i : [] for i in range(n)}
        ans = 0
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            stk = [node]
            while stk:
                node = stk.pop()
                for neiNode in graph[node]:
                    if neiNode in visit:
                        continue
                    stk.append(neiNode)
                    visit.add(neiNode)

        for node in range(n):
            if node not in visit:
                dfs(node)
                ans += 1 
        return ans