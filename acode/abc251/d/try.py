w=int(input())
lst=[i+1 for i in range(99)]

for i in range(1,100):
    lst.append(i*100)
    lst.append(i*10000)
#lst.append(10000) 
#print(298)
print(297)
print(*lst)
