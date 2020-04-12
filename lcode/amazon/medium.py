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
                if a-1 >= 0:
                    next(a-1, b)
                if b-1 >= 0:
                    next(a, b-1)
            return 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += next(i, j)

        return cnt

    #unionfind
    from collections import defaultdict
    def numIslands(self, grid):
            """
            :type grid: List[List[str]]
            :rtype: int
            """
            if len(grid) == 0 or len(grid[0]) == 0:
                    return 0
            totalRow, totalCol = len(grid), len(grid[0])
            parent = defaultdict()
            self.count = 0
            for i in range(totalRow):
                    for j in range(totalCol):
                            if grid[i][j] == "1":
                                    parent[i*totalCol+j] = -1
                                    self.count+=1

            for i in range(totalRow):
                    for j in range(totalCol):
                            if grid[i][j] == "1":
                                    r,c = i,j
                                    for (dr,dc) in [(-1,0),(1,0),(0,-1),(0,1)]:
                                            newRow, newCol = r + dr, c + dc
                                            if 0<=newRow<totalRow and 0<=newCol<totalCol and grid[newRow][newCol] == "1":
                                                    self.union(parent, r*totalCol+c, newRow*totalCol+newCol)
            return self.count

    def find(self, parent, i):
            if parent[i] != -1:
                    return self.find(parent, parent[i])
            else:
                    return i

    def union(self, parent, a, b):
            rootA = self.find(parent,a)
            rootB = self.find(parent,b)
            if rootA != rootB:
                    parent[rootA] = rootB
                    self.count -= 1

