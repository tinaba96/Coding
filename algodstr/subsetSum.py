#from ari book
# p 34

N = int(input())
A = list(map(int, input().split()))
k = int(input())

'''
def dfs(s, i):
    if s == k: 
        return True
    elif i >= N:
        return False


    if dfs(s+A[i], i+1):
        return True

    if dfs(s, i+1):
        return True

    return False




if dfs (0, 0):
    print('Yes')
else:
    print('No')

# O(2**N)
'''


for i in range(2**N):
    ans = 0
    #print('--------')
    t = bin(i)
    b = t[2:]
    for j in range(N-len(b)):
        b = '0'+b
    #print(b)
    for l in range(len(b)):
        if b[l] == '1':
            ans += A[l-2]
            if k == ans:
                print('Yes')
                exit()
        else:
            continue
print('No')

        
# O(N*2**N)






