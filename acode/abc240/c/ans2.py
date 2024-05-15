N, X = map(int, input().split())
dist = set()
dist.add(0)

for i in range(1, N+1):
    a, b = map(int, input().split())
    new_dist = set()
    for now in dist:
        if now + a <= X:
            new_dist.add(now+a)
        if now + b <= X:
            new_dist.add(now+b)
    dist = new_dist

if X in dist:
    print("Yes")
else:
    print("No")
