import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [input().rstrip() for _ in range(n)]
vis = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# from types import GeneratorType
# def bootstrap(f, stack=[]):
#     def wrappedfunc(*args, **kwargs):
#         if stack:
#             return f(*args, **kwargs)
#         else:
#             to = f(*args, **kwargs)
#             while True:
#                 if type(to) is GeneratorType:
#                     stack.append(to)
#                     to = next(to)
#                 else:
#                     stack.pop()
#                     if not stack:
#                         break
#                     to = stack[-1].send(to)
#             return to
#     return wrappedfunc

# @bootstrap
# def dfs(x, y, vis, grid, dx, dy):
#     vis[x][y] = 1
#     if grid[x][y] == '#': yield
#     for i in range(4):
#         a, b = x + dx[i], y + dy[i]
#         if 0<=a<n and 0<=b<m:
#             if vis[a][b]: continue
#             yield dfs(a, b, vis, grid, dx, dy)
#     yield
def encode(x, y): return x << 12 | y
def decode(z): return z >> 12, z & 0xfff
from collections import deque
def bfs(x, y):
    q = deque([encode(x, y)])
    while q:
        x, y = decode(q.popleft())
        vis[x][y] = 1
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if 0<=a<n and 0<=b<m and not vis[a][b] and grid[a][b] == '.':
                q.append(encode(a, b))


ans = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.' and not vis[i][j]:
            bfs(i, j)
            ans += 1
print(ans)



