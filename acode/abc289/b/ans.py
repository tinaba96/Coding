n, m = map(int, input().split())
a= set(map(int, input().split()))

stack = []
ans = []
# for i in range(1, n + 1):
#     stack.append(i) #レ点がないところまでリストstackを作る→
#     if i not in a: #aの中にiが無い場合、読み始める。それまでに貯めていたstackをansに代入する
#         ans.extend(reversed(stack))
#         stack.clear()
#     print(stack,ans)

for i in range(1,n+1):
    if i in a:
        stack.append(i)
        continue
    ans.append(i)
    while len(stack):
        last = stack.pop()
        ans.append(last)
        # print(last,len(stack))
 
print(*ans)
