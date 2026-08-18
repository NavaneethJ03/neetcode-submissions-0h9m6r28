class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac , atl = set() , set()
        rows , cols = len(heights) , len(heights[0])
        res = []
        dirs = [(1 , 0) , (-1 , 0) , (0 , 1) , (0 , -1)]
        def dfs(r , c , prevH , ocean):
            visit = set()
            stk = []
            stk.append([r , c])
            while stk:
                row , col = stk.pop()
                ocean.add((row , col))
                prevH = heights[row][col]
                visit.add((row , col))
                for dr , dc in dirs:
                    nr , nc = dr + row , dc + col
                    if (0 <= nr < rows) and (0 <= nc < cols) and heights[nr][nc] >= prevH and (nr , nc) not in visit:
                        stk.append([nr , nc])

        for r in range(rows):
            dfs(r , 0 , heights[r][0] , pac)
            dfs(r , cols - 1 , heights[r][cols - 1], atl)

        for c in range(cols):
            dfs(0 , c , heights[0][c] , pac)
            dfs(rows - 1 , c , heights[rows - 1][c] , atl)

        return list(pac & atl)
            