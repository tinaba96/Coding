from typing import List

# gloval variable
visit = [[False for _ in range(n)] for p in range(m)]
d = [(-1, -1),(-1,1),(1, -1),(1,1)]

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(m):
            for j in range(n):
                visit[i][j] = True
                if board[m][n] == 'x':
                    continue
                if board[m][n] == 'o':
                    # BFS or DFS

    def check(src, cur):
        for l, r in d:
            if board[l][r] = "0":
                     check(cur, (l,r))


        


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Solution().solve(board)

print(board)

# is it possible to use stack with while loop

