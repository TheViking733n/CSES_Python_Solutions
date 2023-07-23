import sys
from collections import deque
input = lambda :sys.stdin.readline().rstrip()

'''
My first approach was to do multi-source bfs from exit points
This method may be possible to code, but implementation is difficult because of too many edge cases

Better approach would be:
Do a multi-source bfs from all Monster and A.
Trick is to keep 'A' in the end of deque so that it is popped before every monster
This make sures that the all the Monsters move before 'A'
Also update the grid after every move. If 'A' reaches a empty cell first, update it with 'A' and vice-versa
'''


n, m = map(int, input().split())
g = [list(input()) for _ in range(n)]
def isBoundary(x, y): return x == 0 or y == 0 or x == n - 1 or y == m - 1
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
s = 'LRUD'

q = deque()
for i in range(n):
    for j in range(m):
        if g[i][j] == 'A': x0, y0 = i, j
        elif g[i][j] == 'M': q.append((i, j))
q.append((x0, y0))  # Append original position of A in the end
dir = [[-1] * m for _ in range(n)]  # to store direction of A's move
if isBoundary(x0, y0):
    print('YES\n0')
    exit()
dir[x0][y0] = -2
while q:
    x, y = q.popleft()
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if not (0<=a<n and 0<=b<m) or g[a][b] != '.': continue
        g[a][b] = g[x][y]
        if g[a][b] == 'A':  # Only store A's move direction
            dir[a][b] = i
        q.append((a, b))
        
        if g[a][b] == 'A' and isBoundary(a, b):
            ans = []
            while dir[a][b] != -2:
                j = dir[a][b]
                ans.append(s[j])
                a -= dx[j]; b -= dy[j]
            ans.reverse()
            print('YES')
            print(len(ans))
            print(*ans, sep='')
            exit()

print('NO')
