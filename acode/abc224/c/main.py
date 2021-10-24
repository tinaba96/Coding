import math

N = int(input())

#ma = [[] for i in range(H)]
ma = []

for i in range(N):
    x, y = list(map(int, input().split()))
    ma.append((x, y))

cnt = 0
cc = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            dx1 = abs(ma[i][0]-ma[j][0])
            dy1 = abs(ma[i][1]-ma[j][1])
            #d1 = dy1 / dx1
            dx2 = abs(ma[k][0]-ma[i][0])
            dy2 = abs(ma[k][1]-ma[i][1])
            # why dy2 = abs(ma[k][1]-ma[j][1]) does not work?
            # it is because if the two gradient are different only in terms of sign (符号), it will be considered as one line, as shown in the Atcoder video editorial

            dx3 = abs(ma[j][0]-ma[k][0])
            dy3 = abs(ma[j][1]-ma[k][1])

            #print('dx', dx1)
            '''
            if dy2 == 0:
                d2 = 0
            else:
                d2 = dy2 / dx2
            '''
            #print('dy', dy2)
            if dx1 == 0 and dx2 == 0:
                cnt += 1
            elif dy1 == 0 and dy2 == 0:
                cnt += 1
            # why 3 donditions???
            # same reason as above


            elif dx1 != 0 and dx2 != 0 and dy1 != 0 and dy1 != 0 and dy1*dx2 == dy2*dx1 and dy3*dx1 == dy1*dx3 and dy2*dx3 == dy3*dx2:
                cnt += 1
            else:
                cc += 1
#print('cnt', cnt)

print(cc)



#print(ma[0][1])


