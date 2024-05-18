N = int(input())

mp = []

for i in range(N):
    A, B = list(map(int, input().split()))
    mp.append((A,B))

mp.sort()

print(mp)




