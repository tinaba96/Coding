def main():
    from array import array
    n, k = map(int, input().split())
    
    xlist = list(map(int, input().split()))
    
    ok = 0
    ng = (10**18) // k
    
    while ng - ok > 1:
        wj = (ok + ng) // 2
        s = 0
        for x in xlist:
            s += min(x, wj)
        if s >= k * wj:
            ok = wj
        else:
            ng = wj
            
    print(ok)
    
if __name__ == '__main__':
    main()
