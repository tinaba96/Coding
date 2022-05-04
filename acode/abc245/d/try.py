N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = []

for i in range(1, M+2):
    v = C[-i]//A[-1]
    ans.append(v)
    for k in range(1,len(A)):
        C[-i-k] = C[-i-k] - v*A[-1-k]
        #print('a', C[-1-k])

ans = ans[::-1]
ans = list(map(str, ans))

print(' '.join(ans))



