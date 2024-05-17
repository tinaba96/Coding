# more similar to the video editorial

N = int(input())
A = [list(map(int,input().split())) for _ in range(2*N-1)]

ans=0
def dfs(pairs,dancers):
	if len(dancers) == 0:
		global ans
		tmp=0
		for p,q in pairs: tmp ^= A[p][q-1-p]
		ans=max(ans,tmp)
		return
	p=dancers[0]
	for i in range(1,len(dancers)):
		q=dancers[i]
		pairs.append((p,q))
		dfs(pairs,dancers[1:i]+dancers[i+1:])
		pairs.pop()

dfs([],list(range(2*N)))
print(ans)


# = int(input())
# = map(int,input().split())
# = list(map(int,input().split()))
# = input().split()


