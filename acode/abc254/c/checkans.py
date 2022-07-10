n,k=map(int,input().split())
a_l=list(map(int,input().split()))

for i in range(k):
	tmp=[]
	for j in range(i,n,k):
		tmp.append(a_l[j])
	tmp.sort()
	# print("A:",tmp)
	for nj in range(i,n,k):
		a_l[nj]=tmp[nj//k]
		# print(a_l[nj],tmp[nj//k],nj)
# print(a_l)
# print(sorted(a_l))
print("Yes" if a_l==sorted(a_l) else "No")


