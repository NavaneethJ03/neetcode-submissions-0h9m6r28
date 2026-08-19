class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Kahn's Algorithm
        g = defaultdict(list)
        indeg = [0] * numCourses
        for c , v in prerequisites:
            g[v].append(c)
            indeg[c] += 1 

        q = deque([i for i in range(numCourses) if indeg[i] == 0])

        output = []

        while q:
            node = q.popleft()
            output.append(node)

            for v in g[node]:
                indeg[v] -= 1 
                if indeg[v] == 0:
                    q.append(v)

        return output if len(output) == numCourses else []