import itertools


N = int(input())

human = []
l = []

for i in range(N):
    A = list(map(int, input().split()))
    human.append(A)
    l.append(i+1)

M = int(input())

dislike = [[] for i in range(N+1)]


for i in range(M):
    x, y = list(map(int, input().split()))
    dislike[x].append(y)
    dislike[y].append(x)

#l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for v in itertools.permutations(l, N):
    print(v)






