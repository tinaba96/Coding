import copy

n, m = map(int,, input().split())
g = [[] for i in range(n+1)]


for i in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

visited = [False for i in range(n+1)]
visitednum = 0
shimastart = [0 for i in range(n+1)]
shimanum = 0
route = []

def visit(now):
    global route
    global visit
    global visitednum
    visitednum += 1
    visited[now] = True
    route.append(now)
    for j in g[now]:
        if not visited[i]:
            visit(i)

def colorcount(now, colors):
    site = route(now]
    for i in g[site]:
        if colors[i] == colors[site]:
            return 0
        if now == n+1:
            return 1
        kari = 0
        karicolors = copy.copy(colors)
        if shimastart[now+1] == 1:
            karicolors[route[now+1]] = 1
            kari += colorcount(now+1, karicolors)
        else:
            for i in range(3):
                karicolors[route[now+1]] = i+1
                kari += colorcount(now+1, karicolors)
        return kari



for i in range(0, n):
    if not visited[i+1]:
        shimastart[visitednum] = 1
        shimanum = shimanum + 1
        visit(i+1)


colortable = [0 for i in range(n+1)]
colortalble[route[0]] = 1
count = colorcount(0, colortable)

count *= 3**shimanum

print("{}".format(count))


