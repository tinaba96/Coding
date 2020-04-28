

m, n = list(map(int, input().split()))

mat = [[-1]*n for i in range(m)]
for j in range(m):
    mat[j+1] = list(map(int, input().split()))
longest = 0
print(mat)

def path_from(i, j, cnt):
	if mat[i][j+1] == mat[i][j] + 1:
		max = max(path_from(i, j+1, cnt + 1), cnt)
	if mat[i+1][j] == mat[i][j] + 1:
		max = max(path_from(i+1, j, cnt +1), cnt)
	if mat[i-1][j] == mat[i][j] + 1:
		max = max(path_from(i-1, j, cnt + 1), cnt)
	if mat[i][j-1] == mat[i][j] + 1:
		max = max(path_from(i, j-1, cnt + 1), cnt)
	return max

def longest_path(m, n):   # 与えられる行列の大きさ
	for i in range(m):
		for j in range(n):
			cnt = path_from(i, j, 1)
			longest = max(longest, cnt)
	return longest

longest_path(m,n )


