S = str(input())
ss = []

for i in range(len(S)):
    ss.append(S[i])


sort = sorted(ss)
print("".join(sort))


