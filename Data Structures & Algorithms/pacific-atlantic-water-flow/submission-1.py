# if we find for each cell to check whether water will follow to at or pc we have to revision
#  lot's of cell, instead we wil will starte with all the cell who are connected with ocean
# then move to neighbour if value is increasing order (water will flow from cell to ocean not the other wiser)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pc, at = set(), set()
        ROW = len(heights)
        COL = len(heights[0])

        for r in range(ROW):
            # pacifig
            self.dfs(heights, r, 0, 0, pc)
            # at
            self.dfs(heights, r, COL-1, 0, at)

        for c in range(COL):
            # pacifig
            self.dfs(heights, 0, c, 0, pc)
            # at
            self.dfs(heights, ROW-1, c, 0, at)


        ans = []
        for r in range(ROW):
            for c in range(COL):
                if (r, c) in pc and (r, c) in at:
                    ans.append([r, c])
        return ans

    def dfs(self, heights, r, c, prev_height, visited):
        if (r < 0 or 
            r >= len(heights) or 
            c < 0 or 
            c >= len(heights[0]) or 
            (r, c) in visited or 
            heights[r][c] < prev_height
        ):
            return
        

        visited.add((r, c))
        prev_height = heights[r][c]
        self.dfs(heights, r + 1, c, prev_height, visited)
        self.dfs(heights, r - 1, c, prev_height, visited)
        self.dfs(heights, r, c + 1, prev_height, visited)
        self.dfs(heights, r, c - 1, prev_height, visited)


    

        