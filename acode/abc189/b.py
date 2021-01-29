N, X = list(map(int, input().split()))
cnt = 0
for i in range(N):
    cnt += 1
    v, p = list(map(int, input().split()))
    X -= p*v/100
    print(X)
    if X<0:
        print(cnt)
        exit()


print('-1')


