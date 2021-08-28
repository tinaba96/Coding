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

def dfs(used, start, dep, ans):
    for i in range(N+1):
        if dic[start][i] == 1:
            #print(i,'->', used)
            if used[i] == 0:
                used[i] = 1
                dep += 1
                ans = max(ans, dep)
                print('d',dep, '---', i)
                ans = dfs(used, i, dep, ans)
                break
            else:
                continue
    return ans

#print('dic',dic[2])

for i in range(1,N+1):
    used = [0 for j in range(N+1)]
    #print(used)
    print('---new--- (', i, ')')
    dep = 0
    used[i] = 1
    ans = dfs(used, i, dep, ans)
    

print(ans+1)


