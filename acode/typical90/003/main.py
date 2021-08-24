N = int(input())

#dic = {}
dic = [[0 for i in range(N+1)] for j in range(N+1)]


for i in range(N-1):
    a, b = list(map(int, input().split()))
    dic[a][b] = 1
    dic[b][a] = 1
    #print(dic)

dep = 0

def dfs(used, start):
    for i in dic[start]:
        if used[start] == 0:
            used[start] = 1
            dep += 1
            dfs(used, i)
        else:
        continue



for i in dic:
    used = [0 for i in range(N)]
    print(used)



