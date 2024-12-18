"""
Problem: Rotting Oranges
Determine time to rot all oranges using BFS.
"""

from collections import deque

def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh, minutes = 0, 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))  # Rotten orange with time 0
            elif grid[r][c] == 1:
                fresh += 1

    while queue:
        r, c, time = queue.popleft()
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                queue.append((nr, nc, time+1))
                minutes = time + 1

    return minutes if fresh == 0 else -1

grid = [[2,1,1],[1,1,0],[0,1,1]]
print("Minutes to rot all oranges:", orangesRotting(grid))
