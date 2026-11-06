class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i : [] for i in range(n)}
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visit = {}
        def dfs(node , parent):
            if node in visit:
                return bool(visit[node])
            
            visit[node] = 0 
            for nei in graph[node]:
                if nei == parent:
                    continue 

                if not dfs(nei , node):
                    return False 
            visit[node] = 1 
            return True

        return dfs(0, -1) and len(visit) == n