import sys,os,io
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# sys.setrecursionlimit(3000)
input = lambda: sys.stdin.readline().rstrip('\r\n')
print = lambda x: sys.stdout.write(str(x) + '\n')
M, oo = 10**9 + 7, 1 << 30

n, m = map(int, input().split())
g = [input() for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
s = "LRUD"
st = en = -1
for i in range(n):
    for j in range(m):
        if g[i][j] == 'A': st = (i, j)
        elif g[i][j] == 'B': en = (i, j)
par = [[-1] * m for _ in range(n)]
from collections import deque
q = deque([st])
ans = []
par[st[0]][st[1]] = -2
while q:
    x, y = q.popleft()
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if not (0<=a<n and 0<=b<m) or par[a][b] != -1 or g[a][b] == '#': continue
        par[a][b] = i
        q.append((a, b))
        if (a, b) == en:
            print('YES')
            while (a, b) != st:
                j = par[a][b]
                a -= dx[j]
                b -= dy[j]
                ans.append(s[j])
            ans.reverse()
            print(len(ans))
            print(''.join(ans))
            exit()

print('NO')