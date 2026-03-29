class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:


        graph = defaultdict(list)

        visit = set()

        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node , prev):
            if node in visit:
                return False 

            visit.add(node)

            for nei in graph[node]:
                if nei != prev:
                    if not dfs(nei , node):
                        return False 

            return True 

        return dfs(0 , -1) and len(visit) == n

