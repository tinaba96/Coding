n = int(input())
S = input()
ans = -1
cnt = 0
for s in S:
    if s=='o':
        cnt+=1
    else:
        ans = max(ans,cnt)
        cnt = 0
ans = max(ans,cnt)
if ans==0 or S.count('-')==0:
    ans = -1
print(ans)

# you can check number of '-' in order to check whether there is a dango or not
# same as video editorial


