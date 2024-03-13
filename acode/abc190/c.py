'''
N, M = list(map(int, input().split()))
arr = []
for i in  range(M):
    A, B = list(map(int, input().split()))
    arr.append((A, B))
#print(arr[1][0])

K = int(input())

ans = 0

temp = []

#for j in range(K):
 #   C, D = list(map(int, input().split()))
  #  if C not in temp:
   #     temp.append(C)
    #else:
     #   temp.append(D)
#print(temp)


for j in range(K):
    C, D = list(map(int, input().split()))
    temp.append((C, D))

#print(str(bin(2**K)))
cnt = 0
tt = []
tmp = []
for j in range(2**K):
    tmp = str(bin(j))
    tmp = tmp[:2] + '000000000000000000' + tmp[2:]
        
    #print(tmp)
    temporary = []

    for k in range(K):
        temporary.append(temp[k][int(tmp[len(tmp)-1-k])])
    temporary = sorted(temporary) 

    if temporary in tt:
        break
    else:
        tt.append(temporary)

    #print(tt)


    stock = []
    for t in range(M):
        if arr[t][0] in temporary and arr[t][0] not in stock:
            stock.append(arr[t][0])
        if arr[t][1] in temporary and arr[t][1] not in stock:
            stock.append(arr[t][1])
        if arr[t][0] in stock and arr[t][1] in stock:
            cnt += 1

    ans = max(ans, cnt)
    cnt = 0


print(ans)



#TLE
N, M = list(map(int, input().split()))
arr = []
for i in  range(M):
    A, B = list(map(int, input().split()))
    arr.append((A, B))
#print(arr[1][0])

K = int(input())

ans = 0

temp = []

#print(temp)


for j in range(K):
    C, D = list(map(int, input().split()))
    temp.append((C, D))

#print(str(bin(2**K)))
cnt = 0
tmp = []
for j in range(2**K):
    tmp = str(bin(j))
    tmp = tmp[:2] + '000000000000000000' + tmp[2:]

    #print(tmp)
    temporary = []

    for k in range(K):
        temporary.append(temp[k][int(tmp[len(tmp)-1-k])])
    #print(temporary)


    for t in range(M):
        if arr[t][0] in temporary and arr[t][1] in temporary:
            cnt += 1

    ans = max(ans, cnt)
    cnt = 0


print(ans)
'''

#modifying by myself
N, M = list(map(int, input().split()))
arr = []
for i in  range(M):
    A, B = list(map(int, input().split()))
    arr.append((A, B))
#print(arr[1][0])

K = int(input())

ans = 0

temp = []

#print(temp)


for j in range(K):
    C, D = list(map(int, input().split()))
    temp.append((C, D))

#print(str(bin(2**K)))
cnt = 0
tmp = []

k2 = 1<<K
#for j in range(2**K):
for j in range(k2):
    #tmp = str(bin(j))
    #tmp = bin(j)
    #tmp = format(j, 'b')
    #tmp = tmp[:2] + '000000000000000000' + tmp[2:]
    #print(tmp)

    #print(tmp)
    #temporary=dish

    # temporary = [0]*2**K # this was the mistake

    temporary = [0]*(N+1)  # this is the correct one

    for k in range(K):
        if j>>k & 1:
            temporary[temp[k][1]] += 1
        else:
            temporary[temp[k][0]] += 1

        #temporary.append(temp[k][int(tmp[len(tmp)-1-k])])
        #temporary[temp[k][int(tmp[len(tmp)-1-k])]] += 1
        # print(temporary)


    for t in range(M):
        #if arr[t][0] in temporary and arr[t][1] in temporary:
        if temporary[arr[t][0]] != 0 and temporary[arr[t][1]] != 0:
            cnt += 1

    ans = max(ans, cnt)
    cnt = 0


print(ans)





'''
#ans
import itertools

N, M = map(int, input().split())
cond = [tuple(map(int, input().split())) for i in range(M)]
#print(cond)
# ex.[(1, 2), (1, 3), (2, 4), (3, 4)]
K = int(input())
choice = [tuple(map(int, input().split())) for i in range(K)]
ans = 0
for balls in itertools.product(*choice):
    balls = set(balls)
    cnt = sum(A in balls and B in balls for A, B in cond)
    
    if ans < cnt:
        ans = cnt

print(ans)
'''


