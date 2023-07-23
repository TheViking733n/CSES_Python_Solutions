import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = [int(i) - 1 for i in input().split()]
    g[u].append(v)
    g[v].append(u)
from collections import deque
par = [-1] * n
q = deque([0])
par[0] = -2
while q:
    u = q.popleft()
    for v in g[u]:
        if par[v] != -1: continue
        par[v] = u
        q.append(v)
        if v == n - 1:
            ans = [v + 1]
            while v != 0:
                v = par[v]
                ans.append(v + 1)
            ans.reverse()
            print(len(ans))
            print(*ans)
            exit()
print('IMPOSSIBLE')