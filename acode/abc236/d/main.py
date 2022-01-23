import copy
import itertools

N = int(input())

#mp = [[] for i in range(2N)]
mp = [[]]

cnt = []

for i in range(1,2*N):
    cnt.append(i)
    A = list(map(int, input().split()))
    mp.append(A)
cnt.append(2*N)
perm =  list(itertools.permutations(cnt, 2*N))
#for v in itertools.combinations(cnt, 2):
#for v in itertools.permutations(cnt, 2*N):
#for v in itertools.product(cnt, cnt):itertools.combinations(cnt, 2):
    #print(v)
pa = []
tmp = []
c = 0
have = []
ans = 0
alr = set()
#print(perm)
for i in range(len(perm)):
    tmpans = 0
    for j in range(0, 2*N, 2):
        a = min(perm[i][j], perm[i][j+1])
        b = max(perm[i][j], perm[i][j+1])
        if (a, b) in alr:
            break
        else:
            alr.add((a, b))
        tmpans ^= mp[a][b-a-1]
    ans = max(ans, tmpans)
        


print(ans)






