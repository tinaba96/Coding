N = int(input())
S = input()
st = [""]
for i in range(len(S)):
    if S[i] == "(":
        st.append("(")
    elif S[i] == ")":
        if len(st) == 1:
            st[-1] += S[i]
        else:
            st.pop()
    else:
        st[-1] += S[i]
print("".join(st))

'''
N = int(input())
S = list(input())

ans = []
stack = []
for s in S:
    if s == "(":
        Y = ["("]
        stack.append(Y)
    elif s == ")":
        if len(stack) > 0:
            stack.pop()
        else:
            ans.append(")")
    else:
        if len(stack) > 0:
            stack[-1].append(s)
        else:
            ans.append(s)

for s in stack:
    ans.extend(s)

print("".join(ans))
'''
