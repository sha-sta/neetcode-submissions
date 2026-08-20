class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def area(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + area(r + 1, c) + area(r - 1, c) + area(r, c + 1) + area(r, c - 1)
        
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                temp_area = area(r, c)
                if max_area < temp_area:
                    max_area = temp_area
        
        return max_area