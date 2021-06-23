N = int(input())
val = 0
cnt = 0
while True:
    cnt += 1
    val += cnt
    if val >= N:
        break

print(cnt)

