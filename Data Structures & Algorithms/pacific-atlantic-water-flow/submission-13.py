class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows , cols = len(heights) , len(heights[0])
        dirs = [(1,0) , (0,1) , (-1,0) , (0,-1)]
        atl , pac = set() , set()

        def dfs(r , c , ocean):
            stk = [(r , c)]
            while stk:
                row , col = stk.pop()
                if (row , col) not in ocean:
                    prevH = heights[row][col]
                    ocean.add((row , col))
                    for dr , dc in dirs:
                        nr , nc = dr + row , dc + col
                        if (0 <= nr < rows) and (0 <= nc < cols) and heights[nr][nc] >= prevH and (nr , nc) not in ocean:
                            stk.append((nr , nc))


        for r in range(rows):
            dfs(r , 0 , pac)
            dfs(r , cols - 1 , atl)

        for c in range(cols):
            dfs(0 , c , pac)
            dfs(rows - 1 , c , atl)

        return list(atl & pac)