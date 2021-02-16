import math

dict = {}


T = int(input())
flag = False
for t in range(T):
    L, R = list(map(int, input().split()))
    if(L == 0 and R == 0):
        print('1')
        continue
    elif(L == R):
        print('0')
        continue
    else:
        cnt = 0

        gap = R-L+1

        #for g in range(L,gap):
            #cnt += R-L+1 - g

        #ma = gap - R+1

        point = gap-L+1
        tmp = 0
        g = 0

        if flag == True:
            for i in range(len(dict)-1, -1, -1):
                if i <= point:
                    #print(dict_sorted)
                    tmp = dict_sorted[i][1]
                    g = dict_sorted[i][0]
                    break
        
        #tmp = 0
        
        cnt += tmp
        #print('tmp', cnt)
        #print('g', g)

        for i in range(g,point):
            cnt += i

        dict[point] = cnt        

        print(cnt)
        flag = True

        dict_sorted = sorted(dict.items(), key=lambda x:x[0])

#dict.sort()
#print(dict_sorted[-1][1])





