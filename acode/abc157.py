'''
#A
N = 0
N = int(input())
if N%2 == 0:
    print(N//2)
else:
    print(N//2+1)
#B
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

N = int(input())
b = []
for i in range(N):
    b.append(int(input()))
bingo = False
if A[0] in b:
    if A[1] in b:
        if A[2] in b:
            bingo = True

if B[0] in b:
    if B[1] in b:
        if B[2] in b:
            bingo = True


if C[0] in b:
    if C[1] in b:
        if C[2] in b:
            bingo = True

if A[0] in b:
    if B[1] in b:
        if C[2] in b:
            bingo = True


if A[2] in b:
    if B[1] in b:
        if C[0] in b:
            bingo = True

if A[0] in b:
    if B[0] in b:
        if C[0] in b:
            bingo = True

if A[1] in b:
    if B[1] in b:
        if C[1] in b:
            bingo = True

if A[2] in b:
    if B[2] in b:
        if C[2] in b:
            bingo = True

if bingo == False:
    print('No')
else:
    print('Yes')

#C
N, M = list(map(int, input().split()))
ins = False
ans = [0]*N
ok = True
for i in range(M):
    s, c = list(map(int, input().split()))
    if N != 1 and s==1 and c==0:
        ok = False
    if ans[s-1]==0 or ans[s-1]==c:
        ans[s-1] = c
    else:
        ok = False
    if s == 1:
        ins = True
    else:
        ins = False
answer = []
if ok == True:
    for i in range(len(ans)):
        answer.append(str(ans[i]))
    #if N != 1 and ins==False:
    if N != 1 and answer[0]=='0':
        answer[0]='1'
    if N == 1 and M == 0:
        print(0)
    else:
        print(''.join(answer))
else:
    print('-1')
'''
#D
N, M, K = list(map(int, input().split()))
#A = [[0]*N]*N
#上記の方法だと同じリストをN個用意しているだけ
A = [[0 for i in range(N)] for j in range(N)]
for i in range(M):
    a, b = list(map(int, input().split()))
    A[a-1][b-1] += 1
    print(A)


for i in range(K):
    c, d = list(map(int, input().split()))
    A[c-1][d-1] += 1

print(A)

