import copy

N, M, Q = list(map(int, input().split()))
things = []
for n in range(N):
    w, v = list(map(int, input().split()))
    things.append((v, w))

things.sort()
# print('things: ',things)


X = list(map(int, input().split()))

tmp = []

for q in range(Q):
    thing = copy.copy(things)
    ans = 0
    L, R = list(map(int, input().split()))
    tmp = X[:L-1]
    tmp += X[R:]

    tmp.sort()
    # print('tmp: ',tmp)
    for t in range(1, len(tmp)+1):
        for th in range(1, len(thing)+1):
            if tmp[t-1] >= thing[-th][1]:
                ans += thing[-th][0]
                thing.pop(-th)
                break



    print(ans)

