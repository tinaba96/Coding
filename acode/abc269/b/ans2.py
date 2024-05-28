S = [input() for _ in range(10)]
# print(S)

n = 10
a = n
c = n
b = 1
d = 1

for h in range(10):
    for w in range(10):
        if S[h][w] == '#':
            a = min(a, h+1)
            b = max(b, h+1)
            c = min(c, w+1)
            d = max(d, w+1)
        
print(a,b)
print(c,d)


