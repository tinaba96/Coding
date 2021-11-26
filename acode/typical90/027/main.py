N = int(input())
se = set()
ans = []
for i in range(N):
    S = str(input())
    if S not in se:
        se.add(S)
        ans.append(i+1)


for ele in ans:
    print(ele)








