def solution(A, B, C):
    arr = {'a':A, 'b':B, 'c':C}
    arrsort = sorted(list(arr.items()), key = lambda x: x[1], reverse = True)
    ans = []
    tot = A+B+C
    for i in range(tot):
        if len(ans) >= 2 and ans[-1] == arrsort[0][0] and ans[-2] == arrsort[0][0]:
            if arr[arrsort[1][0]] > 0:
                ans.append(arrsort[1][0])
                arr[arrsort[1][0]] -= 1
            else:
                break
            continue
        if arr[arrsort[0][0]] > 0:
            ans.append(arrsort[0][0])
            arr[arrsort[0][0]] -= 1
        else:
            break
    
        arrsort = sorted(list(arr.items()), key = lambda x: x[1], reverse = True)

    return ''.join(ans)


print(solution(0, 0, 0))

