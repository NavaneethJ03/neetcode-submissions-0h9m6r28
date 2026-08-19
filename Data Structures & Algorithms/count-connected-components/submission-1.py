class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = 0 
        g = [[] for _ in range(n)]
        for u , v in edges:
            g[u].append(v)
            g[v].append(u)

        visit = [False] * n

        def dfs(node):
            for nei in g[node]:
                if not visit[nei]:
                    visit[nei] = True 
                    dfs(nei)

        for i in range(n):
            if not visit[i]:
                dfs(i)
                ans += 1 

        return ans
