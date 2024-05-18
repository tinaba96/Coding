N, W = list(map(int, input().split()))

ans = 0

li = []

for i in range(N):
    A, B = list(map(int, input().split()))
    li.append((A, B))

li = sorted(li, reverse=True)

weight = 0

#print(li)

for i in range(N):
    ans += li[i][1]*li[i][0]
    weight += li[i][1]
    #print(ans)
    if weight > W:
        ans -= li[i][1]*li[i][0]
        weight -= li[i][1]
        val = li[i][1]
        for k in range(1, val+1):
            ans += li[i][0]
            weight += 1
            #print(ans)
            if weight > W:
                ans -= li[i][0]
                break
        break

print(ans)

