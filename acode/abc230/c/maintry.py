N, A, B = list(map(int, input().split()))
P, Q, R, S = list(map(int, input().split()))

ans = [['.' for i in range(S-R+1)] for j in range(Q-P+1)]

k = max(1-A, 1-B)
kt = min(N-A, N-B)

diff = kt - k

for i in range(diff+1): # this is too big. can be 10^18
    #print('q')
    #print(A+k+i-1-P)
    #print(B+k+i-1-R)
    #print('---')
    #print(S-R+1)
    #print(Q-P+1)
    if A+k+i-P < 0 or R+B+k+i-R < 0:
        continue
    #ans[A+k+i-1][R+B+k+i-1] = '#'
    ans[A+k+i-P][B+k+i-R] = '#'

k = max(1-A, B-N)
kt = min(N-A, B-1)

diff = kt - k
#print(diff)

for i in range(diff+1): # this is too big. can be 10^18
    #print(A+k+i-1)
    #print(B-k-i-1-P)
    #if (A+k+i-1 >= Q-P+1 or A+k+i-1 < 0) or (B-k-i-1-P >= S-R+1 or B-k-i-1-P < 0):
    #if (A+k+i-1 >= S-R+1 or A+k+i-1 < 0) or (B-k-i-1-P >= Q-P+1 or B-k-i-1-P < 0):
    if A+k+i-P < 0 or B-k-i-R < 0:
        continue
    #print(A+k+i-1)
    #print(B-k-i-1-P)
    #ans[A+k+i-1][B-k-i-1-P] = '#'
    ans[A+k+i-P][B-k-i-R] = '#'


for i in range(len(ans)):
    print(''.join(ans[i]))





