class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ans = 0
        queue = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))

        
        # BFS
        neighbours = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while queue:
            print(queue)
            new_queue = []
            for r, c in queue:
                for r1, c1 in neighbours:
                    n_row = r + r1
                    n_col = c + c1
                    if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]) and grid[n_row][n_col] == 1:
                        grid[n_row][n_col] = 2
                        new_queue.append((n_row, n_col))
            queue = new_queue
            if queue:
                ans += 1

        # if ans == 0:
        #     return - 1
        # else:
        #     return ans
        # check the remaining 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        return ans
