N = int(input())
A = list(map(int, input().split()))


tmp = [0]*max(A)

num = 0
leng = 0

for i in range(max(A)): # 0(n)  max: 10^5
    ans = min(A)*len(A)
    lengt = 0
    num += 1
    for t in range(len(A)):  # O(n) max: 10^4
        A[t] -= 1
        #print(A)
        if A[t] >= 1:
            leng += 1
            #print('leng',leng)
            lengt = max(lengt,leng)
        else:
            leng = 0
    #print('lengt',lengt)
    tmp[i] = max(ans, lengt*(num+1))

#print(tmp)

print(max(tmp))
