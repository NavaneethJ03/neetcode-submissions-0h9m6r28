class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # kahn's Algorithm 

        graph = {i : [] for i in range(n)}
        for u , v in edges:
            graph[v].append(u)
            graph[u].append(v)
        visit = set()
        def dfs(node , parent):
            if node in visit:
                return False 

            visit.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue 
                if not dfs(nei , node):
                    return False 

            return True



        return dfs(0 , -1) and len(visit) == n 
        

                