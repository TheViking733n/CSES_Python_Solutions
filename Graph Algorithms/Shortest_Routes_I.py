import sys
input = sys.stdin.readline
from heapq import heappush, heappop
oo = 1 << 50

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = [int(i) - 1 for i in input().split()]; w += 1
    g[u].append((v, w))
def encode(x, y): return (x << 20 | y)
def decode(z): return z >> 20, z & 0xfffff
src = 0
dis = [oo] * n
dis[src] = 0
q = [encode(0, src)]
# q = SortedList([encode(0, src)])
while q:
    d, u = decode(heappop(q))
    # d, u = decode(q.pop())
    if dis[u] != d: continue   ### REMOVING THIS LINE CAUSES TLE!
    for v, w in g[u]:
        newDis = d + w
        if newDis < dis[v]:
            dis[v] = newDis
            heappush(q, encode(newDis, v))
            # q.add(encode(newDis, v))
print(*dis)
