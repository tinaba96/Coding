s=str(input())
a=[0]*(len(s)+1)
cnt=0
for i in range(len(s)):
        if s[i]=='>' and s[i+1]=='<':
                a[i+1]=0
                for j in range(i+1,len(s),1):
                        if s[j]=='<':
                                a[j+1]=a[j]+1
                        else:
                                break
                for j in range(i,0,-1):
                        if s[j]=='>':
                                a[j]=a[j+1]+1
                        else:
                                break

print(a)
sum=sum(a)
print(sum)

"""
#!/usr/bin/env python3
s = input()
n = len(s)

a = [0] * (n + 1)
b = [0] * (n + 1)
for i in range(n):
    if s[i] == '<':
        a[i + 1] = a[i] + 1
for i in range(n)[::-1]:
    if s[i] == '>':
        b[i] = b[i + 1] + 1
ans = [0] * (n + 1)
for i in range(n + 1):
    ans[i] = max(a[i], b[i])
print(sum(ans))
"""

