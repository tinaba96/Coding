n=int(input())
zahyou={tuple(map(int,input().split())) for _ in range(n)}
cnt=0
for x1,y1 in zahyou:
    for x2,y2 in zahyou:
        if x1!=x2 and y1!=y2 and (x1,y2) in zahyou and (x2,y1) in zahyou:
            cnt+=1
print(cnt//4)


