from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque([])
        # visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))
        

        INF = 2147483647
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c, distance = queue.popleft()
            
            # if grid[r][c] == INF:
            #     grid[r][c] = distance
        
            for r1, c1 in neighbours:
                n_row = r + r1
                n_col = c + c1
                if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]) and grid[n_row][n_col] == INF:
                    grid[n_row][n_col] = distance + 1
                    queue.append((n_row, n_col, distance + 1))
        
            


    # dfs will take more time because dfs go to the farthest node first which instead of 
    # visiting nearby node which cause revisit the nodes multiple time
    # ex. node x was marked distance xx on the first visit but later it was marked x 
    # if we have any ways to ensure that we will visit the nearby node first [BFS] then we do not need to
    # revisit the same node again
    def dfs(self, grid, r, c, distance):
        inf = 2147483647

        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == -1:
            return

        if grid[r][c] == 0 and distance != 0:
            return
        
        # alredy have better value
        if grid[r][c] != 0 and grid[r][c] <= distance:
            return

        if grid[r][c] != 0:
            grid[r][c] = min(grid[r][c], distance)
        
        self.dfs(grid, r + 1, c, distance + 1)
        self.dfs(grid, r - 1, c, distance + 1)
        self.dfs(grid, r, c + 1, distance + 1)
        self.dfs(grid, r, c - 1, distance + 1)

        