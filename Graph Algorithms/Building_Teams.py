import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = [int(i) - 1 for i in input().split()]
    g[u].append(v)
    g[v].append(u)

col = [0] * n
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
def dfs(u, c):
    if col[u]: yield col[u] == c
    col[u] = c
    ok = True
    for v in g[u]:
        ok &= yield dfs(v, 3 - c)
        if not ok: break
    yield ok
ok = True
for i in range(n):
    if not col[i]:
        ok &= dfs(i, 1)
        if not ok: break
if ok: print(*col)
else: print('IMPOSSIBLE')
