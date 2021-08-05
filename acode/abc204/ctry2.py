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

used = [0 for i in range(N+1)]

def count(used, ans, q):
        tmp=q.pop()
        used[tmp] = 1
        for ele in linked_mat[tmp]:
            if used[ele] == 0:
                used[ele] = 1
                q.append(ele)
                ans += 1
                #print('p',ans)
            else:
                continue
        if len(q) == 0:
            return ans
        else:
            ans = count(used, ans, q)
        return ans


for i in range(1, N+1):
    for k in range(N+1):
        used[k] = 0
    q = linked_mat[i]
    #print(q)
    ans += 1
    if len(q) > 0:
        ans += count(used, ans, q)
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
#print(len(buf))
print(ans)

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
