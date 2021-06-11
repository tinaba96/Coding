N = int(input())
T = list(map(int, input().split()))

s = sum(T)

sorted_t = sorted(T, reverse=True)

#print(sorted_t)

a  = 0
b  = 0

for i in range(0, len(sorted_t)):
    if a >= b:
        b += sorted_t[i]
    else:
        a += sorted_t[i]
    #print(a)

print(max(a,b))

