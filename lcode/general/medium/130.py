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
                if (visit[i][j]):
                    continue
                visit[i][j] = True
                if board[m][n] == 'x':
                    continue
                if board[m][n] == 'o':
                    # BFS or DFS
                    stack = []
                    check(,[m,n])

    def check(src, cur):
        for l, r in d:
            if cur[0]+l == src[0] and cur[1]+r == src[1]:
                continue
            if cur[0]+l < 0 or cur[1]+r < 0 or cur[0]+l < m or cur[1]+r < n:
                stack = []
                return
            if board[cur[0]+l][cur[1]+r] == "O":
                board[cur[0]+l][cur[1]+r] = True
                stack.append((l,r))
                check(cur, (l,r))
        return




board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Solution().solve(board)

print(board)

# is it possible to use stack with while loop


