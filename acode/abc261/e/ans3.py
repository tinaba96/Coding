#!/usr/bin/env python3


def main():
    N,C = map(int,input().split())
    C = format(C,"b")
    while len(C) < 30:
        C = "0" + C

    changer = [{"0":0,"1":1} for _ in range(30)]
    
    for _ in range(N):
        T,A = map(int,input().split())
        A = format(A,"b")
        B = ""
        while len(A) < 30:
            A = "0" + A
        for i in range(30):
            dict = changer[i]
            if T == 1:
                dict["0"] = dict["0"]*int(A[i])
                dict["1"] = dict["1"]*int(A[i])
            elif T == 2:
                dict["0"] = max(dict["0"],int(A[i]))
                dict["1"] = max(dict["1"],int(A[i]))
            else:
                dict["0"] = (dict["0"]+int(A[i]))%2
                dict["1"] = (dict["1"]+int(A[i]))%2

            B += str(dict[C[i]])
        C = B
        print(int(C,2))




if __name__ == '__main__':
    main()


