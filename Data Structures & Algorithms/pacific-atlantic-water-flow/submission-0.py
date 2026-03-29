class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac , atl = set() , set()
        nrows , ncols = len(heights) , len(heights[0])
        directions = [(1,0) , (-1,0) , (0,1) , (0,-1)]

        def dfs(r , c , prevHeight , ocean):
            stack = []
            stack.append((r , c , prevHeight))
            while stack:
                row , col , prevHeight = stack.pop()
                if (row , col) not in ocean:
                    ocean.add((row , col))
                for dr , dc in directions:
                    r , c = row + dr , col + dc 
                    if 0 <= r < nrows and 0 <= c < ncols and heights[r][c] >= prevHeight:
                        if (r ,c ) not in ocean:
                            ocean.add((r,c))
                            stack.append((r , c , max(prevHeight , heights[r][c])))
                    

        for r in range(nrows):
            dfs(r , 0 , heights[r][0] , pac)
            dfs(r , ncols - 1 , heights[r][ncols - 1] , atl)

        for c in range(ncols):
            dfs(0 , c , heights[0][c] , pac)
            dfs(nrows - 1 , c , heights[nrows - 1][c] , atl)

        return list(pac & atl)
        


