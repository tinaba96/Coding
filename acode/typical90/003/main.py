N = int(input())

#dic = {}
dic = [[0 for i in range(N+1)] for j in range(N+1)]


for i in range(N-1):
    a, b = list(map(int, input().split()))
    dic[a][b] = 1
    dic[b][a] = 1
    #print(dic)

ans = 0
dep = 0

def dfs(used, start):
    for i in dic[start]:
        if used[start] == 0:
            used[start] = 1
            dep += 1
            dfs(used, i)
        else:
            continue



for i in range(1,N+1):
    used = [0 for j in range(N)]
    #print(used)
    dfs(used, i)
    ans = max(ans, dep)

print(ans+1)


