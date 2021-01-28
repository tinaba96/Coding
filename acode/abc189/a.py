#A
C = str(input())
flag = True
t = C[0]
for i in range(len(C)):
    if C[i] is not t:
        print('Lost')
        exit()


print('Won')

