h, w = map(int, input().split())

s = [input() for _ in range(h)]
t = [input() for _ in range(h)]
s2 = sorted([''.join(map(lambda x: x[i], s)) for i in range(w)])
t2 = sorted([''.join(map(lambda x: x[i], t)) for i in range(w)])

if s2 == t2:
    print("Yes")
else:
    print("No")
