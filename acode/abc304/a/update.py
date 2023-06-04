
N = int(input())

S = []
A = []

min = 10**18

ind = 0
for i in range(N):
    s, a = list(map(str, input().split()))
    a = int(a)
    S.append(s)
    A.append(a)
    if a < min:
        min = a
        ind = i

#print(min)


for i in range(N):
    ans = i+ind
    print(S[ans%N])


