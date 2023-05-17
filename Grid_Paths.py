# s = input()
s = '??????R??????U??????????????????????????LD????D?'
ans = [0]
m = {
    'R': [(0, 1)],
    'L': [(0, -1)],
    'U': [(-1, 0)],
    'D': [(1, 0)],
    '?': [(0, 1), (0, -1), (-1, 0), (1, 0)]
}
mInverse = {
    (0, 1): 'R',
    (0, -1): 'L',
    (-1, 0): 'U',
    (1, 0): 'D'
}

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets

def isValid(x, y, vis):
    return 0 <= x < 7 and 0 <= y < 7 and not vis[x][y]

def connected_components(vis):
    n = len(vis)
    dsu = DSU(n * n)
    one = 0
    for i in range(n):
        for j in range(n):
            if vis[i][j]:
                one += 1
                continue
            if i and not vis[i - 1][j]:
                dsu.union(i * n + j, (i - 1) * n + j)
            if j and not vis[i][j - 1]:
                dsu.union(i * n + j, i * n + j - 1)
    return len(dsu) - one

def movesToString(moves):
    ans = []
    for i in range(1, len(moves)):
        x, y = moves[i]
        px, py = moves[i - 1]
        ans.append(mInverse[(x - px, y - py)])
    return ''.join(ans)

def solve(idx, moves, vis, s, m, ans, ):
    print(idx, ans)
    x, y = moves[-1]
    vis[x][y] = True
    if idx == 48:
        if (x, y) == (6, 0):
            ans[0] += 1

        vis[x][y] = False
        return
    
    if (x, y) == (6, 0):
        vis[x][y] = False
        return

    # Checking if the current move is an adjacent move
    if vis[x+1][y] or vis[x-1][y] or vis[x][y+1] or vis[x][y-1]:
        vis[x][y] = False
        return

    # # Checking if the current move will partition the grid
    # if connected_components(vis) > 1:
    #     vis[x][y] = False
    #     return
    
    for dx, dy in m[s[idx]]:
        if isValid(x + dx, y + dy, vis):
            moves.append((x + dx, y + dy))
            solve(idx + 1, moves, vis, s, m, ans)
            moves.pop()
    

    vis[x][y] = False

solve(0, [(0, 0)], [[0]*7 for i in range(7)], s, m, ans)
print(ans[0])




'''
Below code is code but its recursive function is not much efficient so TLE

s = input()
ans = [0]
m = {
    'R': [(0, 1)],
    'L': [(0, -1)],
    'U': [(-1, 0)],
    'D': [(1, 0)],
    '?': [(0, 1), (0, -1), (-1, 0), (1, 0)]
}

def isValid(x, y, vis):
    return 0 <= x < 7 and 0 <= y < 7 and not vis[x][y]

def solve(idx, moves, vis, s, m, ans):
    print(idx)
    x, y = moves[-1]
    vis[x][y] = True
    if idx == 47:
        if (x, y) == (6, 0):
            ans[0] += 1
        vis[x][y] = False
        return
    
    if (x, y) == (6, 0):
        vis[x][y] = False
        return

    for dx, dy in m[s[idx]]:
        if isValid(x + dx, y + dy, vis):
            moves.append((x + dx, y + dy))
            solve(idx + 1, moves, vis, s, m, ans)
            moves.pop()
    vis[x][y] = False

solve(0, [(0, 0)], [[0]*7 for i in range(7)], s, m, ans)
print(ans)

'''