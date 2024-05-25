n = int(input())
if n == 1:
    print('Yes')
    exit()
s = [complex(*map(int, input().split())) for _ in range(n)]
t = [complex(*map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j or abs(s[1] - s[0]) != abs(t[j] - t[i]):
            continue
        s2 = [(k - s[0]) * (t[j] - t[i]) for k in s]
        t2 = [(k - t[i]) * (s[1] - s[0]) for k in t]
        s2.sort(key=lambda x: (x.real, x.imag))
        t2.sort(key=lambda x: (x.real, x.imag))
        for k, l in zip(s2, t2):
            print(k)
            print(l)
            if k != l:
                break
        else:
            print('Yes')
            exit()
print('No')
