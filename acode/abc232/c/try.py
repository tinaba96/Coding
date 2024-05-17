N, M = list(map(int, input().split()))

if M == 0:
    print('Yes')
    exit()

mapA = [[] for i in range(N+1)]
mapC = [[] for j in range(N+1)]

for i in range(M):
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
#for ele in list(itertools.permutations(range(N))):
flag = True
#P = list(ele)
#P = [0, 2, 4, 7, 1, 5, 6, 3]
P = [2, 1, 0, 3]
#for i in range(N):
#    P[i] += 1

AA = [[] for j in range(len(mapA))]


for i in range(1,len(mapA)):
   for j in range(len(mapA[i])):
       tmp = P.index(mapA[i][j]-1)+1
       AA[P.index(i-1)+1].append(tmp)

#print(len(mapA))
print(AA)
print(mapC)
#print(mapC)
#print(P)
for i in range(1, len(mapA)):
#for i in range(1, len(mapA)):
    #print('A', AA[i])
    #print('C', mapC[P[i-1]])
    #print(i, ':', P[i-1])
    #if set(AA[i]) != set(mapC[P[i-1]+1]):
    if set(AA[i]) != set(mapC[i]):
    #if set(AA[i]) != set(mapC[P[i-1]]):
        print(i)
        print('No')
        print(set(AA[i]))
        print(set(mapC[i]))
        #print(set(mapC[P[i-1]+1]))
        flag = False
        
#if flag == False:
#    continue
#print(P)
if flag:
    print('Yes')
    exit()

print('No')

