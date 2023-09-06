def inputs(type_=int):
    return map(type_,input().split())

def input_list(type_=int):
    return list(map(type_,input().split()))

import heapq
def dijkstra(edges, start, _goal=None):
    """ 経路の表現
            [終点, 辺の値]
            A, B, C, D, ... → 0, 1, 2, ...とする """
    node = [float('inf')] * len(edges)    #スタート地点以外の値は∞で初期化
    node[start] = 0     #スタートは0で初期化

    node_name = []
    heapq.heappush(node_name, [0, start])

    while len(node_name) > 0:
        #ヒープから取り出し
        _, min_point = heapq.heappop(node_name)
        
        #経路の要素を各変数に格納することで，視覚的に見やすくする
        for factor in edges[min_point]:
            goal = factor[0]   #終点
            cost  = factor[1]   #コスト

            #更新条件
            if node[min_point] + cost < node[goal]:
                node[goal] = node[min_point] + cost     #更新
                #ヒープに登録
                heapq.heappush(node_name, [node[min_point] + cost, goal])

    return node if not _goal else node[_goal]

N1,N2,M = inputs()
edges1 = [[] for _ in range(N1)]
edges2 = [[] for _ in range(N2)]
for _ in range(M):
    a,b = inputs()
    if a < N1:
        edges1[a-1].append((b-1,1))
        edges1[b-1].append((a-1,1))
    else:
        edges2[a-1-N1].append((b-1-N1,1))
        edges2[b-1-N1].append((a-1-N1,1))

# print(edges1)
# print(edges2)

shortest_root1 = dijkstra(edges1,0)
shortest_root2 = dijkstra(edges2,N2-1)

# print(shortest_root1)
# print(shortest_root2)

print(max(shortest_root1)+max(shortest_root2)+1)
