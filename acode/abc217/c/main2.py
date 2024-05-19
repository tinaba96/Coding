N = int(input())
A = list(map(int, input().split()))
arr = []
for i in range(N):
    arr.append((A[i], i))

arr = sorted(arr)
ans = []
#print(arr[0][1])

for j in range(N):
    tmp = int(arr[j][1])+1
    ans.append(str(tmp))

#print(list(ans))


ans =' '.join(ans)
print(ans)

