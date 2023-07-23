
import sys,os,io
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# sys.setrecursionlimit(3000)
input = lambda: sys.stdin.readline().rstrip('\r\n')
# print = lambda x: sys.stdout.write(str(x) + '\n')
M, oo = 10**9 + 7, 1 << 30

class DisjointSetUnion:
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


n, m = map(int, input().split())
dsu = DisjointSetUnion(n)
for _ in range(m):
    u, v = [int(i) - 1 for i in input().split()]
    dsu.union(u, v)
sets = len(dsu)
p = list(set(dsu.find(i) for i in range(n)))
print(len(p)-1, flush=False, file=sys.stdout)
for i in range(len(p)-1):
    u, v = p[i], p[i+1]
    print(f'{u + 1} {v + 1}', flush=False, file=sys.stdout)


