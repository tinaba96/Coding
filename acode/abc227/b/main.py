N = int(input())
S = list(map(int, input().split()))

mp = set()
t = []

a = 0
b = 0
val = 0

for a in range(1, 1000):
    for b in range(1, 1000):
        v = 4*a*b + 3*a + 3*b
        mp.add(v)

cnt = 0
#print(mp)

for s in S:
    if s not in mp:
        cnt += 1

print(cnt)


