#尺取り法

N = int(input())

ans=10**30
j=10**6
for i in range(10**6+1):
    while (i+j)*(i**2+j**2)>=N and j>=0:
        ans=min(ans,(i+j)*(i**2+j**2))
        j-=1
    '''
    if ans==N or j<0:
        break
    '''

print(min(ans,10**(18)))
