A, B, W = list(map(int, input().split()))

w = 1000*W

temp_min = 1001
temp_max = 0

for i in range(1001):
    for j in range(1001):
        if ( w == A*i + B*j):
            temp_min = min(temp_min, i+j)
            temp_max = max(temp_max, i+j)
print(temp_max)
if(temp_min==1001 or temp_max==0):
    print('UNSATISFIABLE')
else:
    print(temp_min, temp_max)

for i in range(A, B):
    for ele in range(abs(a-b)+1):
        for num in range(1000):
            temp = ele*num*i



