N = int(input())

A = list(map(int, input().split()))

cnt = {}
#cnt = [0 for i in range(200)]

for ele in A:
    if ele not in cnt:
        cnt[ele] = 0
    cnt[ele] += 1


print(cnt)
ans = 0

for i in range(1, len(cnt)):
    ans += abs()*cnt[i-1]*cnt[i]

# I think, in order to loop only the number of the element instead of 200, i have to have those value as an array. eg. [(value, cnt), (value, cnt),..]



#ans
from collections import Counter
n = int(input())
a = [int(_) for _ in input().split()]
c = Counter(a)
ans = 0
for i in range(-200, 200):
    for j in range(i+1, 201):
        ans += c[i]*c[j]*(i-j)**2
print(ans)


