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
for j in range(2**K):  #O(2**k)
    tmp = str(bin(j))
    tmp = tmp[:2] + '000000000000000000' + tmp[2:]

    #print(tmp)
    temporary = []

    for k in range(K): #O(K)
        temporary.append(temp[k][int(tmp[len(tmp)-1-k])])  # append takes time  #O(K)
    #print(len(temporary)) #16


    for t in range(M): #O(M)
        if arr[t][0] in temporary and arr[t][1] in temporary: #O(K)  When I remove this, the computation time became almost 1/3, which tells us that this part is the bottleneck in terms of the time complexity.
            cnt += 1

    ans = max(ans, cnt)
    cnt = 0


print(ans)
# O(k2(K*K+M*K))

'''

#last TLE -> the reason of this is that the size of the temporary array is too big when k=16
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
for j in range(k2):  # O(k2)
    #tmp = str(bin(j))
    #tmp = bin(j)
    #tmp = format(j, 'b')
    #tmp = tmp[:2] + '000000000000000000' + tmp[2:]
    #print(tmp)

    #print(tmp)
    #temporary=dish
    temporary = [0]*2**k

    for k in range(K): #O(K)
        if j>>k & 1:
            temporary[temp[k][1]] += 1
        else:
            temporary[temp[k][0]] += 1

        #temporary.append(temp[k][int(tmp[len(tmp)-1-k])])
        #temporary[temp[k][int(tmp[len(tmp)-1-k])]] += 1
        #print(temporary)


    for t in range(M): #0(M)
        #if arr[t][0] in temporary and arr[t][1] in temporary:
        if temporary[arr[t][0]] != 0 and temporary[arr[t][1]] != 0:
            cnt += 1

    ans = max(ans, cnt)
    cnt = 0


print(ans)


# O(k(N+K+M))

'''

