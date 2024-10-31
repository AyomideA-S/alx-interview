# Island Perimeter

Implement a function `def island_perimeter(grid):` that calculates the perimeter of the island described in `grid`.

## Description

You are given a grid of integers where:

- `0` represents water
- `1` represents land
- Each cell is a square with a side length of 1
- Cells are connected horizontally or vertically (not diagonally)
- The grid is rectangular, width and height do not exceed 100

The grid is completely surrounded by water, and there is only one island (or none). The island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island).

## Requirements

- `grid` is a list of lists of integers
- The function should return an integer representing the perimeter of the island

## Process

The `island_perimeter` function calculates the perimeter by following these steps:

1. **Iterate Through the Grid**: It traverses each cell in the 2D `grid`.
2. **Identify Land Cells**: For every cell with a value of `1` (representing land), it adds `4` to the perimeter.
3. **Check for Adjacent Land Cells**:
    - **Above**: If the current land cell has a land cell above it (`i > 0` and `grid[i - 1][j] == 1`), it subtracts `2` from the perimeter to account for the shared edge.
    - **Left**: If the current land cell has a land cell to its left (`j > 0` and `grid[i][j - 1] == 1`), it subtracts another `2` for the shared edge.
4. **Return the Total Perimeter**: After processing all cells, the function returns the calculated `perimeter`.

This method ensures that each land cell contributes the correct number of edges to the total perimeter by adjusting for any shared edges with adjacent land cells.
