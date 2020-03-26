import sys

def comb(f1, f2):
    return lambda x:f1(f2(x))

REV = lambda ls: list(reversed(ls))  #左右反転 
USD = lambda ls: [len(ls)-x-1 for x in ls]  #上下反転
T90 = lambda ls: [ls.index(x) for x in range(len(ls))]  ##90度回転
T180 = comb(USD, REV)  #180度回転
T270 = comb(T90, T180)  #270度回転
D1 = comb(REV, T90) #対角線での反転その1
D2 = comb(USD, T90)  #対角線での反転

def is_different(cols, sols):
    return all(tuple(op(cols)) not in sols for op in (REV, USD, T90, T180, T270, D1, D2))

def queen_ok(ls, row1):
    return all(abs(row1-row)!=col+1 for col, row in enumerate(ls))

def nqueen(n):
    def qiter(cols, rows):
        if rows:
            for i in rows:
                if queen_ok(cols, i):
                    qiter((i,)+cols, rows-{i})
        elif is_different(cols, sols):
            sols.add(cols)
   
    sols = set()
    qiter(tuple(), frozenset(range(n)))
    return sols

if __name__=='__main__':
    sols=nqueen(int(sys.argv[1]))
    print('N of solutions:', len(sols))
    for sol in sols:
        print(sol)








