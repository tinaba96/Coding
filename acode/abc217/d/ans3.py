def format_input(argv):
        l, q = [0] * 2
        query = []
        if len(argv) == 1:
            l, q = list(map(int, input().split()))
            query = [list(map(int, input().split())) for i in range(q)]
        '''
        else:
            from random import randint as rng
            l = rng(1, 10**9)
            q = rng(1, 10**5)
            query = [[rng(1, 2), rng(1, l-1)] for i in range(q)]
            print(l, q)
            [print(" ".join(list(map(str, query[i])))) for i in range(q)]
        '''

        return l, q, query

def build(q):
    B = max(int(pow(q, 1/2)), 1) # I think this is done for reducing the complexity since the length of each block gets smaller which leads to higher speed oc the access. (I think O(Q**(3/2)))
    #  constant factor （定数倍）will not do anything. -> it works for  B = 2*max(int(pow(q, 1/2)), 1)  as well
    # However, it also works for B = q//2. -> this will not make a big difference for the time complexity (still O(Q*Q) but it will be AC. I think it is because of the tiny speed up by doing this, which I think it is the same reason for the one using array.array explained in here
    # https://kanpurin.hatenablog.com/entry/2021/09/05/163703
    key = []
    child = [[]]
    tree = {"B": B, "key": key, "child": child}
    return tree

import bisect
def insert(tree, key):
    index = bisect.bisect_left(tree["key"], key)
    block = tree["child"][index]
    bisect.insort(block, key)
    if len(block) > tree["B"]:
        k = tree["B"] // 2
        tree["key"].insert(index, block[k])
        tree["child"].insert(index+1, block[k+1:])
        tree["child"][index] = block[:k]
        print('yes')
    print(tree)

def lower_bound(tree, key):
    index = [None, None] # first for 'key' and second for 'child'
    index[0] = bisect.bisect_left(tree["key"], key)
    index[1] = bisect.bisect_left(tree["child"][index[0]], key)
    print('index', index)
    return index

def prev(tree, index):
    index = index.copy()
    if index[1] == 0:
        index[0] -= 1
        index[1] = len(tree["child"][index[0]])
    else:
        index[1] -= 1
    return index

def index_to_key(tree, index):
    if index[1] == len(tree["child"][index[0]]):
        return tree["key"][index[0]]
        #if index[0] == len(tree["key"]):
        #    return None
    else:
        return tree["child"][index[0]][index[1]]

def get_answer(vals):
    answer = []
    l, q, query = vals

    tree = build(q)

    insert(tree, 0)
    insert(tree, l)

    for i in range(q):
        key = query[i][1]
        if query[i][0] == 1:
            insert(tree, key)
        else:
            r = lower_bound(tree, key)
            l = prev(tree, r)
            #print(index_to_key(tree, r))
            answer.append(index_to_key(tree, r) - index_to_key(tree, l))

    return answer

if __name__ == '__main__':
    import sys
    #print(sys.argv)
    vals = format_input(sys.argv)

    ans = get_answer(vals)
    [print(x) for x in ans]

# key is the index where the wood is cut

'''
25 16
1 3
1 9
1 14
1 4
1 5
1 11
1 10
1 6
1 7
1 13
1 8
1 17
1 16
2 3
2 19
2 18
{'B': 4, 'key': [], 'child': [[0]]}
{'B': 4, 'key': [], 'child': [[0, 25]]}
{'B': 4, 'key': [], 'child': [[0, 3, 25]]}
{'B': 4, 'key': [], 'child': [[0, 3, 9, 25]]}
yes
{'B': 4, 'key': [9], 'child': [[0, 3], [14, 25]]}
{'B': 4, 'key': [9], 'child': [[0, 3, 4], [14, 25]]}
{'B': 4, 'key': [9], 'child': [[0, 3, 4, 5], [14, 25]]}
{'B': 4, 'key': [9], 'child': [[0, 3, 4, 5], [11, 14, 25]]}
{'B': 4, 'key': [9], 'child': [[0, 3, 4, 5], [10, 11, 14, 25]]}
yes
{'B': 4, 'key': [4, 9], 'child': [[0, 3], [5, 6], [10, 11, 14, 25]]}
{'B': 4, 'key': [4, 9], 'child': [[0, 3], [5, 6, 7], [10, 11, 14, 25]]}
yes
{'B': 4, 'key': [4, 9, 13], 'child': [[0, 3], [5, 6, 7], [10, 11], [14, 25]]}
{'B': 4, 'key': [4, 9, 13], 'child': [[0, 3], [5, 6, 7, 8], [10, 11], [14, 25]]}
{'B': 4, 'key': [4, 9, 13], 'child': [[0, 3], [5, 6, 7, 8], [10, 11], [14, 17, 25]]}
{'B': 4, 'key': [4, 9, 13], 'child': [[0, 3], [5, 6, 7, 8], [10, 11], [14, 16, 17, 25]]}
index [0, 1]
index [3, 3]
index [3, 3]
3
8
8
'''
