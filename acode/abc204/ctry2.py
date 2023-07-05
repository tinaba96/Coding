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
        tmp=q.pop(0)
        #print('pop', tmp)
        #print(linked_mat[tmp])
        used[tmp] = 1

        #print('first', ans)

        #print('p',used)
        for ele in linked_mat[tmp]:
            if used[ele] == 0:
                used[ele] = 1
                q.append(ele)
                ans += 1
                #print('middle',ans)
            else:
                continue
        if len(q) == 0:
            return ans
        else:
            ans = count(used, ans, q)
            #print(ans)
        return ans


for i in range(1, N+1):
    for k in range(N+1):
        used[k] = 0
    #print('initial', used)
    q = [i]
    #print('q',q)
    ans += 1
    used[i] = 1
    #print('beforefinal', ans)
    ans += count(used, 0, q)
    #print(i)
#print(possible_mat[i])
print(ans)

