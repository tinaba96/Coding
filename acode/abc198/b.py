
#A, B, W = list(map(int, input().split()))


N = str(input())

cnt_z = 0
for i in N:
    if i == '0':
        cnt_z += 1
    else:
        break



cnt_zr = 0
N_rev = N[::-1]
for t in N_rev:
    if t == '0':
        cnt_zr += 1
    else:
        break
if N == N_rev:
    print('Yes')
    exit()


#print(cnt_z)

    
if cnt_zr > cnt_z:
    N_comp1 = N[:len(N)-cnt_zr+cnt_z]
    N_comp2 = N_rev[cnt_zr-cnt_z:]
else: 
    print('No')
    exit()

#print(N_comp1)

if N_comp1 == N_comp2:
    print('Yes')
else:
    print('No')



