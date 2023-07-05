import sys
import resource

sys.setrecursionlimit(4000)
#print(sys.getrecursionlimit())
# naximum recursion is 1000

N, M = list(map(int, input().split()))

linked_set = {}

linked_mat = [ [] for j in range(N+1)]
#linked_mat = [ [0 for i in range(N)] for j in range(N)]

ans = 0

check = []

for m in range(1, M+1):
    a, b = list(map(int, input().split()))
    linked_mat[a].append(b)
    if a not in check:
        check.append(a)
    #linked_mat[a][b] = 1

#print(linked_mat)

possible_mat = [ [] for j in range(N+1)]

#n = linked_mat[]

#print(check)

already = []


def count(a, c):
    for j in range(len(linked_mat[a])):
        if linked_mat[a][j] in c:
            continue
        else:
            c.append(linked_mat[a][j])
            #possible_mat[a].append(linked_mat[a][j])
            if linked_mat[a][j] in check:
                count(linked_mat[a][j], c)
            else:
                continue

for i in range(1, N+1):
    count(i, possible_mat[i])
    #print(i)
    #print(possible_mat[i])

buf = []

for j in range(1, N+1):
    #print(possible_mat[j])
    for k in range(len(possible_mat[j])):
        buf.append((j, possible_mat[j][k]))
    if (j,j) not in buf:
        buf.append((j, j))
    #print('buf', buf)
    #print(j, 'ok')

    #ans += len(set(possible_mat[j]))

an = []
print(len(buf))
i = 0
'''
for e in buf:
    i += 1
    print(i, "/", len(buf))
    if e not in an:
        an.append(e)
#print('an', an)

print(len(an))
'''
