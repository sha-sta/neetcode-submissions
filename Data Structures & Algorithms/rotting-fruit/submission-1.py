class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque

        sources = []
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    sources.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        q = deque(sources)
        minutes = 0

        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()
                for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1
        
        return minutes if fresh == 0 else -1


