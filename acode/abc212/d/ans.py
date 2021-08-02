def main():
    import heapq
    q = int(input())
    lst = []
    heapq.heapify(lst)
    shift = 0
    addnumber = 0
    for i in range(q):
        query = list(map(int,input().split()))
        if query[0]==1:
            val = query[1]
            heapq.heappush(lst,val-addnumber)

        if query[0]==2:
            addnumber += query[1]

        if query[0]==3:
            minn = heapq.heappop(lst)
            print(minn + addnumber)
if __name__ == '__main__':
    main()
