print()
'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''


def test(grid):
    row = len(grid)
    colum = len(grid[0])
    # print(row,colum)

    def helper(grid, r, c):
        row = len(grid)
        colum = len(grid[0])
        # print(r,c)
        if r >= 0 and c >= 0 and r < row and c < colum:
            return
        grid[r][c] = "0"
        helper(grid, r - 1, c)
        helper(grid, r + 1, c)
        helper(grid, r, c - 1)
        helper(grid, r, c + 1)

    res = 0
    for i in range(row):
        for j in range(colum):
            if grid[i][j] == "1":

                helper(grid, i, j)
    return res

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(test(grid))








'''
java :
class Solution {
  void dfs(char[][] grid, int r, int c) {
    int nr = grid.length;
    int nc = grid[0].length;

    if (r < 0 || c < 0 || r >= nr || c >= nc || grid[r][c] == '0') {
      return;
    }

    grid[r][c] = '0';
    dfs(grid, r - 1, c);
    dfs(grid, r + 1, c);
    dfs(grid, r, c - 1);
    dfs(grid, r, c + 1);
  }

  public int numIslands(char[][] grid) {
    if (grid == null || grid.length == 0) {
      return 0;
    }

    int nr = grid.length;
    int nc = grid[0].length;
    int num_islands = 0;
    for (int r = 0; r < nr; ++r) {
      for (int c = 0; c < nc; ++c) {
        if (grid[r][c] == '1') {
          ++num_islands;
          dfs(grid, r, c);
        }
      }
    }

    return num_islands;
  }
}
'''



