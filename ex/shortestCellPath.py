'''

Shortest Cell Path
In a given grid of 0s and 1s, we have some starting row and column sr, sc and a target row and column tr, tc. Return the length of the shortest path from sr, sc to tr, tc that walks along 1 values only.

Each location in the path, including the start and the end, must be a 1. Each subsequent location in the path must be 4-directionally adjacent to the previous location.

It is guaranteed that grid[sr][sc] = grid[tr][tc] = 1, and the starting and target positions are different.

If the task is impossible, return -1.



input:
grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: 8
(The lines below represent this grid:)
1111
0001
1111

grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: -1
(The lines below represent this grid:)
1111
0001
1011

'''

from collections import deque
def shortestCellPath(grid, sr, sc, tr, tc):
	"""
	@param grid: int[][]
	@param sr: int
	@param sc: int
	@param tr: int
	@param tc: int
	@return: int
	"""
	queue = deque()
	queue.append((sr, sc, 0))
	seen = set()
	seen.add((sr, sc))
	
	R = len(grid)
	C = len(grid[0])

	while queue:
		r, c, depth = queue.popleft()
		if r == tr and c == tc: return depth
		for (nr, nc) in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
			if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1 and (nr, nc) not in seen:
				queue.append((nr, nc, depth + 1))
				seen.add((nr, nc))
	return -1

grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr, sc, tr, tc = 0, 0, 2, 0
print(shortestCellPath(grid, sr, sc, tr, tc))

'''
def shortestCellPath(grid, sr, sc, tr, tc):
	"""
	@param grid: int[][]
	@param sr: int
	@param sc: int
	@param tr: int
	@param tc: int
	@return: int
	"""
	start = [sr, sc]
    target = [tr, tc]

    move = [(1,1), (-1, -1), (1, -1), (-1, 1)]

    def count(cur_r, cur_c, shortestVal):
        if cur_r == tr and cur_c == tc:
            return shortestVal
        for r, c in move:
            if cur_r+r < 0 or cur_c+c < 0:
                continue
            else:
                if grid[cur_r+r][cur_c+c] == '1':
                    count(cur_r+r, cur_c+c, shortestVal+1)
                else:
                    continue 
'''
'''
function shortestCellPath(grid, sr, sc, tr, tc):
    queue = Queue()
    queue.add((sr, sc, 0))
    seen = new HashSet()
    seen.add((sr, sc))

    while queue:
        r, c, depth = queue.popfront()
        if r == tr and c == tc: return depth
        for (nr, nc) in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1 and (nr, nc) not in seen:
                queue.append((nr, nc, depth + 1))
                seen.add((nr, nc))

    return -1
'''
'''
Time Complexity: O(R*C), where R, C are the number of rows and columns in grid. We might visit every square in the grid. It's worth noting that typically in a breadth-first-search, the time complexity is O(V+E) where V = R * C is the number of nodes in the graph, and E is the number of edges. Since E <= 4*V, this is O(V+E) = O(V) = O(R * C).

Space Complexity: O(R*C), the space to store queue and seen.
'''
# https://www.tryexponent.com/courses/swe-practice/shortest-cell-path
