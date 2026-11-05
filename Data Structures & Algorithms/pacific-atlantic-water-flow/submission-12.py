class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows , cols = len(heights) , len(heights[0])
        dirs = [(1,0) , (0,1) , (-1,0) , (0,-1)]

        atl , pac = set() , set()

        def dfs(r , c , ocean):
            stk = [[r , c]]
            while stk:
                r , c = stk.pop()
                if (r , c) in ocean:
                    continue
                prevH = heights[r][c]
                ocean.add((r , c))
                for dr , dc in dirs:
                    nr , nc = dr + r , dc + c
                    if (0 <= nr < rows) and (0 <= nc < cols) and (nr , nc) not in ocean and heights[nr][nc] >= prevH:
                        stk.append([nr , nc])

        for r in range(rows):
            dfs(r , 0 , pac)
            dfs(r , cols - 1 , atl)

        for c in range(cols):
            dfs(0 , c , pac)
            dfs(rows - 1 , c , atl)

        return list(atl & pac)
