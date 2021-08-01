N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 100100100100100100100100

A.sort()
B.sort()

#print(A)
#print(B)

#why WA
'''
for n in range(N):
    for m in range(M):
        ans = min(ans, abs(A[n]-B[m]))
        if A[n] < B[m]:
            print('this')
            break
    print('ok')

print(ans)
'''


if N <= 4 or M <= 4 :
    for n in range(N):
        for m in range(M):
            ans = min(ans, abs(A[n]-B[m]))
    print(ans)
    exit()

B.append(10010010000000000000)
#print(B)

for n in range(N):
    l = 0
    r = M
    mi = M//2
    ans = min(ans, abs(A[n]-B[0]))
    ans = min(ans, abs(A[n]-B[M-1]))
    while r-l > 0:
        ans = min(ans, abs(A[n]-B[mi]))
        if ans == 0:
            print(ans)
            exit()
        if A[n] < B[mi]:
             r = mi
        else:
             l = mi
        if (r+l)//2 == r or (r+l)//2 == l:
            break

        mi = (r+l)//2


print(ans)




