# https://www.youtube.com/watch?v=Bbp_W3Jpk9I

N = str(input())
length = len(N)

ans = 1
tmpSet = set()
start_p = 0
end_p = -1

for i in range(length):
    v = N[i]
    end_p = i
    if v not in tmpSet:
        tmpSet.add(v)
    else:
        for j in range(start_p, end_p):
            start_char = N[j]
            if start_char == v:
                start_p = j+1
                break
            else:
                tmpSet.remove(start_char)
    ans = max(ans, end_p-start_p+1)

print(ans)








