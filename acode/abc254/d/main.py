import math
N = int(input())
ans  = 0
#target = sqrt(N)+1

l = []
def cnt(v):
    i = 1
    j = v
    ans = 2
    while i <= j:
        i += 1
        if v%i == 0:
            ans += 2
            j = v//i
            #print(i, j, ans)
            if i == j:
                ans -= 1
                break
        else:
            continue

    return ans






for i in range(N+1):
    if math.sqrt(i)%1 != 0:
        continue
    else:
        l.append(i)


print(l)



now = 0
'''
for i in range(N):
    now += cnt(i)
'''

print(now)

print(cnt(N))



