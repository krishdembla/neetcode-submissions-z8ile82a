class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0

        # visited = set()

        def dfs(r,c):
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == "0":
                return #we ignore if the cell is water
            
            #now we know we have a 1
            grid[r][c] = "0" #change so we know it has been visited

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i,j)
        return count

