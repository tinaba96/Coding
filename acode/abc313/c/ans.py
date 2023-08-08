n = int(input())
a = sorted(list(map(int, input().split())))
s = sum(a)
d = s // n
r = s % n

# print(n, a, s, d, r)
ans = 0

for i in range(n - r):
    ans += abs(a[i] - d)
for i in range(n - r, n):
    ans += abs(a[i] - (d + 1))

print(ans // 2)


