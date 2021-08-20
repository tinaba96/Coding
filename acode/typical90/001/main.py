N, L = list(map(int, input().split()))
K = int(input())
A = list(map(int, input().split()))



left = 0
right = 100000

while left <= right:
    #print('right', right)
    #print('left', left)
    mid = (left+right)//2
    #print('mid', mid)
    tmp = 0
    cnt = 0
    minus = 0
    #flag = False
    for a in range(len(A)):
        tmp = A[a] - minus
        #print(A[a], minus)
        if tmp >= mid:
            minus = A[a]
            cnt += 1
            '''
            if tmp == mid:
                flag = True
            '''
        if cnt == K:
            if mid < L-A[a]:
                left = mid+1
                '''
                if flag:
                    print(mid)
                    exit()
                '''
            elif mid == L-A[a]:
                print(mid)
                exit()
            else:
                right = mid-1
            break
        elif a == len(A)-1 and cnt < K:
            right = mid-1
print(mid)
            
#think about the # of K after looking all the A instead of L-A[a]

