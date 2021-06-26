N = int(input())

mps = [[0 for j in range(N)] for i in range(N)]
mpt = [[0 for j in range(N)] for i in range(N)]

tmps = []
tmpt = []
check = [0 for i in range(N)]


for s in range(N):
    a, b = list(map(int, input().split()))
    # mps[a][b] = 1 
    tmps.append([a,b])

for t in range(N):
    a, b = list(map(int, input().split()))
    #mpt[a][b] = 1 
    tmpt.append([a,b])

print(tmpt)

for n in range(N):
    for x in range(-10, 10):
        for y in range(-10, 10):
            tmps[n][0] += x
            tmps[n][1] += y
            if tmps[n] == tmpt[n]:
                check[n] = 1
flag = True
for i in range(N):
    if check[i] != 1:
        flag = False
if flag == True:
    print('Yes')
    exit
    

for k in range(N):
    (tmps[k][0], tmps[k][1]) = (-tmps[k][0], tmps[k][1])

for n in range(N):
    for x in range(-10, 10):
        for y in range(-10, 10):
            tmps[n][0] += x
            tmps[n][1] += y
            if tmps[n] == tmpt[n]:
                check[n] = 1
flag = True
for i in range(N):
    if check[i] != 1:
        flag = False
if flag == True:
    print('Yes')
    exit
    

for k in range(N):
    (tmps[k][0], tmps[k][1]) = (tmps[k][0], -tmps[k][1])

for n in range(N):
    for x in range(-10, 10):
        for y in range(-10, 10):
            tmps[n][0] += x
            tmps[n][1] += y
            if tmps[n] == tmpt[n]:
                check[n] = 1
flag = True
for i in range(N):
    if check[i] != 1:
        flag = False
if flag == True:
    print('Yes')
    exit
    



for k in range(N):
    (tmps[k][0], tmps[k][1]) = (tmps[k][1], tmps[k][0])

for n in range(N):
    for x in range(-10, 10):
        for y in range(-10, 10):
            tmps[n][0] += x
            tmps[n][1] += y
            if tmps[n] == tmpt[n]:
                check[n] = 1
flag = True
for i in range(N):
    if check[i] != 1:
        flag = False
if flag == True:
    print('Yes')
    exit


print('No')
                        
                        



