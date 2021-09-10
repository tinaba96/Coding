# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
L = []
push, pop = L.append, L.pop
def main(N, K):
    if N < K: return
    if N == K:
        print(''.join(L + ([')'] * K)))
        return
    push('(')
    main(N - 1, K + 1)
    pop()
    if K >= 1:
        push(')')
        main(N - 1, K - 1)
        pop()

if __name__ == '__main__':
    N = int(input())
    main(N, 0)


#bit全探索でもOK
#O(N*2**N)かな
#それともO(N**2*2**N)かな <- appendそれぞれに対してn回実行してるから。
#それでもitertools.permutations()より早いの？



