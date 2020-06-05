class Solution:
    import collections
    def checkRecord(self, s: str) -> bool:
        c = collections.Counter(s)
        if c['A'] >= 2:
            return False
        for i in range(2, len(s)):
            if s[i-2] == s[i-1] == s[i] == 'L':
                return False
        else:
            return True
    
    class Solution:
    def checkRecord(self, s: str) -> bool:
        cnt = 0
        for i in range(len(s)):
            if s[i] == 'A':
                cnt += 1
            if cnt == 2:
                return False
            if i > 1 and s[i-2] == s[i-1] == s[i] == 'L':
                return False
        return True

    #fastest
    class Solution:
    def checkRecord(self, s: str) -> bool:
        cnt = 0
        for i in range(len(s)):
            if s[i] == 'A':
                cnt += 1
            if cnt == 2:
                return False
        return s.find('LLL')<0

    #組み込み関数find()が早いことを確認するための検証
    for i in range(len(s)):
        if s[i] == 'L':
            return false
    #20ms
    s.find('L')
    #16ms
    #組み込み関数の方が少し早いことがわかる。その理由は分からない。


    #another methomd
    import re
    def checkRecord(self, s: str) -> bool:
        return not re.match(".*(A.*A|LLL).*", s)

    '''
    Regular Expression of the string containing two or more than two A ′s will be .∗A.∗A.∗ and the regular expression of the string containing substring LLL will be .∗LLL.∗. We can merge this two regex using ∣ and form a regex of string containing either more than one A or containing substring LLL. Then regex will look like: .∗(A.∗A∣LLL).∗. We will return true only when the string doesn't matches this regex.
    '''


    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        def cnt(time):
            ti = 0
            for i in range(N):
  
                if time[1] == times[i][0]:
                    ti += cnt(times[times.index(i)])
                    c  += 1
                    return time[2]
            return ti

        c = 0
        cnt(K)
        if c < N:
            return -1
        else:
            return ti

    
    #dfs
    class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        dist = {node: float('inf') for node in xrange(1, N+1)}

        def dfs(node, elapsed):
            if elapsed >= dist[node]: return
            dist[node] = elapsed
            for time, nei in sorted(graph[node]):
                dfs(nei, elapsed + time)

        dfs(K, 0)
        ans = max(dist.values())
        return ans if ans < float('inf') else -10


    #Dijkstra O(N^2)
    class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float('inf') for node in xrange(1, N+1)}
        seen = [False] * (N+1)
        dist[K] = 0

        while True:
            cand_node = -1
            cand_dist = float('inf')
            for i in xrange(1, N+1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i

            if cand_node < 0: break
            seen[cand_node] = True
            for nei, d in graph[cand_node]:
                dist[nei] = min(dist[nei], dist[cand_node] + d)

        ans = max(dist.values())
        return ans if ans < float('inf') else -1

    #heep version O(NlogN)
    class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, K)]
        dist = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist: continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d+d2, nei))

        return max(dist.values()) if len(dist) == N else -1



