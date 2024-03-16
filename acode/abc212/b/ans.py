x = list(map(int,input()))
flag = True
samef = True
for i in range(3):
    if x[i]!=x[i+1]: samef = False
    if (x[i]+1)%10!=x[i+1]: flag = False
if flag or samef:
    print("Weak")
else:
    print("Strong")
