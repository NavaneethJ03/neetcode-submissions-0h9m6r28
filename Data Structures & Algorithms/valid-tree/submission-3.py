class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        graph = [[] for _ in range(n)]

        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node , parent):
            if node in visit:
                return False 

            visit.add(node)

            for nei in graph[node]:
                if nei == parent:
                    continue 
                else:
                    if not dfs(nei , node):
                        return False 

            return True 

        return dfs(0 , -1) and len(visit) == n