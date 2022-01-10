N, M = list(map(int, input().split()))

if M == 0:
    print('Yes')
    exit()

mapA = [[] for i in range(N+1)]
mapC = [[] for j in range(M+1)]

for i in range(N):
    A, B = list(map(int, input().split()))
    mapA[A].append(B)
    mapA[B].append(A)

for i in range(M):
    C, D = list(map(int, input().split()))
    mapC[C].append(D)
    mapC[D].append(C)

#P = [3, 2, 1, 4]
#R = [1, 2, 3, 4]

import itertools

for ele in list(itertools.permutations(range(N))):
    flag = True
    P = list(ele)
    for i in range(N):
        P[i] += 1

    AA = [[0 for i in range(len(mapA[j]))] for j in range(len(mapA))]

    for i in range(len(mapA)):
        for j in range(len(mapA[i])):
            AA[i][j] = P.index(mapA[i][j])+1

#print('sa')
#print(AA)
#print(mapC)
    for i in range(1, len(mapA)):
        #print('A', AA[i])
        #print('C', mapC[P[i-1]])
        if set(AA[i]) != set(mapC[P[i-1]]):
            #print('No')
            flag = False
            
    if flag == False:
        continue
    #print(P)
    print('Yes')
    exit()

print('No')



