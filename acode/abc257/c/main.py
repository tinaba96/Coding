N = int(input())
S = str(input())
W = list(map(int, input().split()))



child = []
adult = []
newS = []

dat = []
sdat = []

for i in range(N):
    dat.append((S[i], W[i]))
sdat = sorted(dat, key=lambda x:x[1])

for i in range(N):
    newS.append(sdat[i][0])

for i in range(N):
    if S[i] == '1':
        adult.append(W[i])
    else:
        child.append(W[i])

answer = len(adult)
ans = len(adult)

for i in range(len(newS)):
    if newS[i] == '0':
        ans += 1
    else:
        ans -= 1
    answer = max(answer, ans)

print(answer)

