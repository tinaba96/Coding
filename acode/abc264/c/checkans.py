import sys
input = sys.stdin.readline

h1, w1 = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h1)]
h2, w2 = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(h2)]
for s in range(1<<h1):
    if sum(s>>k&1 for k in range(h1)) != h2:
        continue
    for t in range(1<<w1):
        if sum(t>>k&1 for k in range(w1)) != w2:
            continue
        c = []
        for i in range(h1):
            if s>>i&1:
                c.append([])
                for j in range(w1):
                    if t>>j&1:
                        c[-1].append(a[i][j])
        if c == b:
            print("Yes")
            exit()
print("No")
