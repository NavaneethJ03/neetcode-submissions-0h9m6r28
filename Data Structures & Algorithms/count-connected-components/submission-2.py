class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.count = 0 
        graph = {i : [] for i in range(n)}
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visit = set()
        def dfs(node):
            if node in visit:
                return

            visit.add(node)

            for nei in graph[node]:
                dfs(nei)

        for i in range(n):
            if i not in visit:
                self.count += 1 
                dfs(i)

        return self.count