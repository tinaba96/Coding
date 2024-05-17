t = int(input())

def f(t):
    return t**2+2*t+3

ans = f(f(f(t)+t)+f(f(t)))
print(ans)

