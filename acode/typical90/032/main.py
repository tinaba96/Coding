import itertools


N = int(input())

human = []
l = []

for i in range(N):
    A = list(map(int, input().split()))
    human.append(A)
    l.append(i+1)

M = int(input())

dislike = [[] for i in range(N+1)]

ans = 100100100100

for i in range(M):
    x, y = list(map(int, input().split()))
    dislike[x].append(y)
    dislike[y].append(x)
#l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for v in itertools.permutations(l, N):
    score = human[v[0]-1][0]
    hate = False
    for i in range(1, N):
        if v[i] in dislike[v[i-1]] or v[i-1] in dislike[v[i]]:
            hate = True
            break
        else:
            score += human[v[i]-1][i]
    #score += humman[v[N-1]][N-1]
    if hate == False:
        ans = min(ans, score)

if ans == 100100100100:
    print(-1)
else:
    print(ans)




