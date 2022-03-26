N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = []
i = 1
while True:
    v = C[-i]//A[-1]
    ans.append(v)
    for k in range(1,len(A)):
        C[-i-k] = C[-i-k] - v*A[-1-k]
        #print('a', C[-1-k])
    #if C[0] == 0:
    #    break
    i += 1
    if i == len(C)-len(A)+2:
        break
ans.sort(reverse=True)
ans = list(map(str, ans))

print(' '.join(ans))



