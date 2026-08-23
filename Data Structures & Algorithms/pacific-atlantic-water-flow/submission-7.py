class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl , pac = set() , set()
        rows , cols = len(heights) , len(heights[0])
        dirs = [(0 , 1) , (0 , -1) , (1 , 0) , (-1 , 0)]
        
        def dfs(r , c , prevH , ocean):
            visit = set()
            stk = [[r , c]]
            while stk:
                r , c = stk.pop()
                ocean.add((r , c))
                prevH = heights[r][c]
                visit.add((r , c))

                for dr , dc in dirs:
                    nr , nc = r + dr , c + dc
                    if (0 <= nr < rows) and (0 <= nc < cols) and (nr , nc) not in visit and heights[nr][nc] >= prevH:
                        stk.append([nr , nc])
                        

        for r in range(rows):
            dfs(r , 0 , heights[r][0] , pac)
            dfs(r , cols - 1 , heights[r][cols - 1] , atl)

        for c in range(cols):
            dfs(0 , c , heights[0][c] , pac)
            dfs(rows - 1 , c , heights[rows - 1][c] , atl)

        return list(atl & pac)


