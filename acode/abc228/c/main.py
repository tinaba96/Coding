import copy

N, K = list(map(int, input().split()))

score = [0 for i in range(N+1)]

for i in range(N):
    P = list(map(int, input().split()))
    score[i] = sum(P)

order = copy.copy(score)
order = sorted(score, reverse=True)

border = order[K-1]

#print(score)
#print(K)
#print(order)

for i in range(N):
    if border <= 300+score[i]:
        print('Yes')
    else:
        print('No')


