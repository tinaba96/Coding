n = int(input())
s = input()
stack = []
l = 0
for i in range(n):
  if s[i] == ')' and l:
    l -= 1
    while stack:
      if stack.pop() == '(':
        break
  else:
    l += (s[i] == '(')
    stack.append(s[i])
print(''.join(stack))
