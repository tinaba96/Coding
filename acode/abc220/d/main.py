N = int(input())
A = list(map(int, input().split()))

ans = [0]*10
out = [0]*10


ans[(A[0]+A[1])%10] += 1
ans[A[0]*A[1]%10] += 1

print(ans)


for i in range(N-1):
    for k in range(10):
        if ans[k] > 0:
            #need one more array
            ans[(k+A[i+1])%10] += 1
            ans[k*A[i+1]%10] += 1
        


'''
for i in range(N-1):
    ans[(A[i]+A[i+1])%10] += 1
    ans[A[i]*A[i+1]%10] += 1
'''


print(out)



