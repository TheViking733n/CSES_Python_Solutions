import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = [int(i) - 1 for i in input().split()]
    g[u].append(v)
    g[v].append(u)
 
vis = [0] * n
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
 
@bootstrap
def dfs(u, pa, path):
    path.append(u)
    vis[u] = 1
    for v in g[u]:
        if vis[v] == 2 or v == pa: continue
        if vis[v] == 1:
            ans = [v + 1]
            while path[-1] != v:
                ans.append(1 + path.pop())
            ans.append(v + 1)
            print(len(ans))
            print(*ans)
            exit()
        yield dfs(v, u, path)
    path.pop()
    vis[u] = 2
    yield
for i in range(n):
    if not vis[i]: dfs(i, -1, [])
print('IMPOSSIBLE')