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
