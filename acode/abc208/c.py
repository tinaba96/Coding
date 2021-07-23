N, K = list(map(int, input().split()))
a = list(map(int, input().split()))
tmp = 0
if K >= N:
    tmp = K//N
    k = K%N
else:
    k = K

arr = sorted(a)
# print(arr)
if k >= 1:
    t = arr[k-1]
else:
    t = -1

for i in range(N):
    if a[i] <= t:
        a[i] = tmp+1
    else:
        a[i] = tmp
    # print(a)

for j in range(N):
    print(a[j])


