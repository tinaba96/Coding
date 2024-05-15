def d_moves_on_binary_tree():
    N, X = [int(_) for _ in input().split()]
    S = input()

    stack = []
    for ch in S:
        if not stack:
            stack.append(ch)
        else:
            if stack[-1] in ('L', 'R') and ch == 'U':
                stack.pop()
            else:
                stack.append(ch)
    ans = X
    for ch in stack:
        if ch == 'U':
            ans //= 2
        elif ch == 'L':
            ans *= 2
        elif ch == 'R':
            ans = ans * 2 + 1
    return ans

print(d_moves_on_binary_tree())
