"""

Question: Count Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Sample Input 1
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

Sample Output 1
1

Sample Input 2
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

Sample Output 2 
3

"""

def mark_land(grid, row, column,m, n):
    if row>= n or column < 0 or row < 0 or column >= m or grid[row][column] != "1":
      return
    grid[row][column] = "2"
    mark_land(grid, row + 1, column, m, n)
    mark_land(grid, row, column + 1, m, n)
    mark_land(grid, row - 1, column, m, n)
    mark_land(grid, row, column - 1, m, n)
  
def count_island(grid):
  #write your code here
  n = len(grid)
  m = len(grid[0])
  
  islands = 0
  for i in range(0, n):
    for j in range(0,m):
      if grid[i][j] == "1":
        mark_land(grid, i, j, m, n)
        islands += 1
  return islands
      


if __name__ == "__main__":
  input_matrix = [
  ["1","0","0","0","1"],
  ["0","1","0","1","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","0"]
]
  print(count_island(input_matrix))





