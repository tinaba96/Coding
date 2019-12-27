def dfs(v):
  dist = [-1] * (n+1)
  dist[v] = 0
  stack = [v]
  while stack:
    now = stack.pop()
    dw = dist[now] + 1
    for ne in graph[now]:
      if dist[ne] >= 0:
        continue
      dist[ne] = dw
      stack.append(ne)
  return dist
