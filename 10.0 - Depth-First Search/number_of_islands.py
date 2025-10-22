"""
Number of Islands

Given an m × n grid consisting of 1s (land) and 0s (water), return the number 
of islands. An island is formed by connecting adjacent 1s vertically or horizontally.

Example:
Input:
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
Output: 3
Explanation:
- The first island consists of the top-left 1s
- The second island consists of the middle 1
- The third island consists of the bottom-right 1s

Input:
grid = [
    ["1","1","0","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
Output: 1
Explanation: There is only one connected island
"""
def count_number_of_islands(grid: list[list[int]]) -> int:
    num_rows = len(grid)
    num_cols = len(grid[0])

    def get_neighbors(coord):
        res = []
        row, col = coord
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]

        for i in range(len(delta_row)):
            r = row + delta_row[i]
            c = col + delta_col[i]
            if 0 <= r < num_rows and 0 <= c < num_cols:
                res.append((r, c))

        return res


    def dfs(coord):
        r, c = coord
        if grid[r][c] == 0:
            return
        grid[r][c] = 0
        for neighbor in get_neighbors(coord):
            nr, nc = neighbor
            if grid[nr][nc] == 1:
                dfs(neighbor)

    count = 0
    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == 1:
                dfs((r, c))
                count += 1

    return count

if __name__ == "__main__":
    grid = []
    num_rows = int(input())
    num_cols = int(input())
    
    for _ in range(num_rows):
        row = [int(x) for x in input().split()]
        grid.append(row)
    
    result = count_islands(grid)
    print(result)
