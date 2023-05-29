
class SegmentTree:
    def __init__(self, n, e, arr=None):
        self.n = n
        self.log = (n-1).bit_length()
        self.size = 1<<self.log       
        self.e = e
        self.data = [e] * (self.size<<1)
        self.len = [1] * (self.size<<1)        
        if arr: self.build(arr)
            
    def _update(self, i): self.data[i] = op(self.data[i<<1], self.data[i<<1|1])
    
    def build(self, data):
        """Builds the segment tree [Called Automatically upon __init__]. O(n)"""
        for i, a in enumerate(data, self.size): self.data[i] = a
        for i in range(self.size-1, 0, -1):
            self._update(i)
            self.len[i] = self.len[i<<1] + self.len[i<<1|1]
    
    def update(self, k, x):
        """Updates the k-th element (0-indexed) to x. O(log n)"""
        k += self.size
        self.data[k] = x
        for i in range(1, self.log+1): self._update(k>>i)
    def __setitem__(self, k, x):
        k += self.size
        self.data[k] = x
        for i in range(1, self.log+1): self._update(k>>i)
            
    def add(self, k, x):
        """Adds x to the k-th element (0-indexed). O(log n)"""
        k += self.size
        self.data[k] += x
        for i in range(1, self.log+1): self._update(k>>i)
    def __iadd__(self, k, x):
        k += self.size
        self.data[k] += x
        for i in range(1, self.log+1): self._update(k>>i)

    def get(self, k):
        """Returns the k-th element (0-indexed). O(1)"""
        return self.data[k+self.size]
    def __getitem__(self, k):
        return self.data[k+self.size]
    
    def query(self, l, r):
        """Returns op(a[l], ..., a[r-1]). O(log n)"""
        sml, smr = self.e, self.e
        l += self.size
        r += self.size
        while l < r:
            if l&1:
                sml = op(sml, self.data[l])
                l += 1
            if r&1:
                r -= 1
                smr = op(self.data[r], smr)
            l >>= 1
            r >>= 1
        return op(sml, smr)
    
    def query_all(self):
        """Returns op(a[0], ..., a[n-1]). O(1)"""
        return self.data[1]
    
    def max_right(self, l, func):
        """Returns max r such that func(op(a[l], ..., a[r-1])) holds. O(log n)"""
        if l == self.n: return self.n
        l += self.size
        sm = self.e
        while True:
            while l%2 == 0: l >>= 1
            if not func(op(sm, self.data[l])):
                while l < self.size:
                    l <<= 1
                    if func(op(sm, self.data[l])):
                        sm = op(sm, self.data[l])
                        l += 1
                return l - self.size
            sm = op(sm, self.data[l])
            l += 1
            if l & -l == l: break
        return self.n
    
    def min_left(self, r, func):
        """Returns min l such that func(op(a[l], ..., a[r-1])) holds. O(log n)"""
        if r == 0: return 0
        r += self.size
        sm = self.e
        while True:
            r -= 1
            while r > 1 and r%2: r >>= 1
            if not func(op(self.data[r], sm)):
                while r < self.size:
                    r = r << 1 | 1
                    if func(op(self.data[r], sm)):
                        sm = op(self.data[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = op(self.data[r], sm)
            if r & -r == r: break
        return 0
    
    def __repr__(self) -> str:
        return f"STree({[self[i] for i in range(self.n)]})"
"""
Usage of SegmentTree(n, e, arr):
    op is a binary operation on S, e.g. op = lambda x, y: x + y
    N is the length of the array, e.g. N = 10
    e is the identity element of op, e.g. e = 0
    A is the initial array, e.g. A = [1] * N
"""
op = max
e = 0
def func(x):
    return x < k

n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))
k = 0
seg = SegmentTree(n, e, arr)
ans = []
for i in range(m):
    k = queries[i]
    idx = seg.max_right(0, func)
    if idx != n:
        seg[idx] -= k
    ans.append((-1 if idx == n else idx) + 1)
print(*ans)