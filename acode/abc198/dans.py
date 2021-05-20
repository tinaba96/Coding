# ans
from itertools import permutations
def main():
    sset = set()
    S = []
    for _ in range(3):
        s = list(input())
        S.append(s)
        if len(sset) == 0:
            sset = set(s)
        else:
            for ss in set(s):
                sset.add(ss)
    if len(sset) > 10:
        print("UNSOLVABLE")
        exit()
    str_i = [str(i) for i in range(10)]
    for comb in permutations(str_i, len(sset)):
        c2i = {s:i for s, i in zip(sset, comb)}
        SS = []
        for s in S:
            ss_s = ""
            for ss in s:
                if ss_s == "" and c2i[ss] == '0':
                    break
                ss_s += c2i[ss]
            if ss_s == "":
                SS.append(ss_s)
            else:
                SS.append(int(ss_s))
        NG = set(["", 0])
        if SS[0] in NG or SS[1] in NG or SS[2] in NG:
            continue
        if SS[0] + SS[1] == SS[2] and len(str(SS[0])) == len(S[0]) and len(str(SS[1])) == len(S[1]) and len(str(SS[2])) == len(S[2]):
            print(*SS, sep='\n')
            exit()
    print("UNSOLVABLE")
main()






