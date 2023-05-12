N,K = map(int,input().split())
A = set(map(int,input().split()))
ans = 0

x = 0

while x in A:
    x += 1

print(min(x, K))

# video editorial
