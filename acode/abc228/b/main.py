N, X = list(map(int, input().split()))
A = list(map(int, input().split()))


cnt = set()
cnt.add(X)

x = X

while True:
    t = A[X-1]
    if t not in cnt:
        cnt.add(t)
        X = t
    else:
        break;

print(len(cnt))


