class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i : [] for i in range(n)}
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visit = set()

        def dfs(node):
            stk = [node]

            while stk:
                node = stk.pop()
                if node not in visit:
                    visit.add(node)

                for nei in graph[node]:
                    if nei not in visit:
                        stk.append(nei)
        ans = 0             
        for i in range(n):
            if i not in visit:
                dfs(i)
                ans += 1

        return ans