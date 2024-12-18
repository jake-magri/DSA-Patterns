"""
Problem: Number of Islands
Given a 2D grid of '1's (land) and '0's (water), count the number of connected islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

Approach:
Use DFS to explore all connected '1's starting from an unvisited '1'.
Mark cells as visited to avoid revisiting them.

Time Complexity: O(M x N) where M and N are grid dimensions.
"""

def dfs(grid, i, j):
    # Base case: Out of bounds or water
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
        return
    
    # Mark the current cell as visited
    grid[i][j] = '0'

    # Explore all 4 directions (up, down, left, right)
    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i, j - 1)

def num_islands(grid):
    if not grid:
        return 0

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':  # Start DFS for each unvisited land cell
                dfs(grid, i, j)
                count += 1  # Increment the island count
    return count

# Example grid
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print("Number of Islands:", num_islands(grid))
