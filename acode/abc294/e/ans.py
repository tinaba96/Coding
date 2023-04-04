L, N1, N2 = map(int, input().split())
vl1, vl2 = [], []
for _ in range(N1):
    vl1.append(tuple(map(int, input().split())))
for _ in range(N2):
    vl2.append(tuple(map(int, input().split())))

ans = 0
idx = 0
remain = vl2[0][1] # this  is the next target for l2
l1 = 0
l2 = 0
for v in vl1:
    l1 += v[1]
    while l1 > l2: # this contine looping when "remain" is updating. breakes when l1 == l2
        ex = min(l1 - l2, remain) # diff
        if v[0] == vl2[idx][0]:
            ans += ex
        remain -= ex 
        if remain == 0: # when ex == remain
            idx += 1
            if idx == N2:
                break
            remain = vl2[idx][1]
        l2 += ex
print(ans)

# this is the approach which set the next l2 target as "remain" and see the l1 target one by one. and, move "remain" to the next when l1 target exceed the "remain" 
# l2 is kind of previous positon (pt in video editorial)

# l2: base, l1: target of l1, remain: target of l2

# a little bit different implementation from the video editorial

