from bisect import bisect, bisect_left, bisect_right

N = int(input())
S = input()
W = list(map(int, input().split()))

adalt = []
child = []

for i in range(N):
    if S[i] == "0":
        child.append(W[i])
    else:
        adalt.append(W[i])

adalt.sort()
child.sort()
if len(adalt)==0:
    print(len(child))
    exit()
elif len(child) == 0:
    print(len(adalt))
    exit()
ans = max(len(adalt),len(child))

for i in range(len(adalt)):
    f_x = len(adalt)-i
    f_x += bisect_left(child,adalt[i])
    ans = max(ans,f_x)
print(ans)
