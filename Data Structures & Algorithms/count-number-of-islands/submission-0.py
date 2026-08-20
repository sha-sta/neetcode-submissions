class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        def flood (r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            flood(r+1, c)
            flood(r-1, c)
            flood(r, c+1)
            flood(r, c-1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    flood(r, c)
                    num_islands += 1
        
        return num_islands
