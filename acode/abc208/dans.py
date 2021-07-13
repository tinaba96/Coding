def fuc(d):
    answer=0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j]= min(d[i][j],d[i][k]+d[k][j])
                if d[i][j] < 1<<60:
                    answer+=d[i][j]
    return answer
n,m = map(int,input().split())
d = [[1<<60 for i in range(n)] for i in range(n)]
for i in range(n):
    d[i][i] = 0
for i in range(m):
    a,b,c = map(int,input().split())
    d[a-1][b-1] = c
print(fuc(d))


