def main(lines):
    N, K, A = list(map(int, lines.split()))

    ans = (K - 1 + A) % N
    if (ans == 0):
        return N
    else:
        return ans
      
if __name__ == "__main__":
    print(main(input()))


'''

N,K,A=map(int,input().split())
print((K+A-2)%N+1)



'''
