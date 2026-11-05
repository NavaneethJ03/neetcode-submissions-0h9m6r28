from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2**31 - 1
        q = deque()
        
        # Seed all treasure rooms
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        
        while q:
            r, c = q.popleft()
            nd = grid[r][c] + 1          # next distance
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                # Only expand into unvisited empty rooms
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                    grid[nr][nc] = nd
                    q.append((nr, nc))