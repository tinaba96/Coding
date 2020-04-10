#200
class Solution:
    def numIslands(self, grid:List[List[str]]) -> int:
        cnt = 0
        def next(a, b):
            if grid[a][b] == '0':
                grid[a][b] = '-1'
                return 0
            if grid[a][b] == '1':
                grid[a][b] = '2'
                if b+1 < len(grid[0]):
                    next(a, b+1)
                if a+1 < len(grid):
                    next(a+1, b)

            return 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    cnt += next(i, j)
                    if i+1 < len(grid):
                        cnt += next(i+1, j)
                    if j+1 < len(grid[0]):
                        cnt += next(i, j+1)

        return cnt

