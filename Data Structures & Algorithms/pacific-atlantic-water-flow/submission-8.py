class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows , cols = len(heights) , len(heights[0])
        dirs = [(1 , 0) , (0 , 1) , (-1 , 0) , (0 , -1)]
        atl , pac = set() , set()
        
        def dfs(r , c , prevH , ocean):
            
            stk = [[r , c]]
            ocean.add((r , c))
            while stk:
                row , col = stk.pop()
                prevH = heights[row][col]
                for dr , dc in dirs:
                    nr , nc = row + dr , col + dc 
                    if (0 <= nr < rows) and (0 <= nc < cols) and (nr , nc) not in ocean and heights[nr][nc] >= prevH:
                        stk.append([nr , nc])
                        ocean.add((nr , nc))


        for r in range(rows):
            dfs(r , 0 , heights[r][0] , pac)
            dfs(r , cols - 1 , heights[r][cols - 1] , atl)
        for c in range(cols):
            dfs(0 , c , heights[0][c] , pac)
            dfs(rows - 1 , c , heights[rows - 1][c] , atl)

        return list(atl & pac)