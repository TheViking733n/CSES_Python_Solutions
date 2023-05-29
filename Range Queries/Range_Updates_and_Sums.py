from __future__ import division, print_function
import os,sys
from io import BytesIO, IOBase
from random import randint, randrange
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip


from math import ceil, floor, factorial, log10
# from math import log,sqrt,cos,tan,sin,radians
from bisect import bisect_left, bisect_right
from collections import deque, Counter, defaultdict
# from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right
# from decimal import *
# from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
# from collections import OrderedDict
# from itertools import permutations


M=1000000007
# M=998244353
# INF = float("inf")
INF = 9223372036854775807
PI = 3.141592653589793
R = randrange(2, 1 << 32)
# R = 0          # Enable this for debugging of dict keys in myDict

# ========================= Main ==========================








class LazySegmentTree:
    def __init__(self, data, padding = 0):
        """initialize the lazy segment tree with data"""
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        
        self.data = [padding] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(1, _size)):
            self.data[i] = self.data[2 * i] + self.data[2 * i + 1]     
        self._lazy = [1,0] * (2 * _size)
 
    def _push(self, idx):
        """push query on idx to its children"""
        # Let the children know of the queries
        idx *= 2
        a = self._lazy[idx]
        b = self._lazy[idx + 1] >> 1
        self._lazy[idx] = 1
        self._lazy[idx + 1] = 0
        
        self.data[idx] = a * self.data[idx] + b
        self.data[idx + 1] = a * self.data[ idx + 1] + b
        
        idx *= 2
        self._lazy[idx] = a * self._lazy[idx] 
        self._lazy[idx + 1] = a * self._lazy[idx + 1] + b
        self._lazy[idx + 2] = a * self._lazy[idx + 2]
        self._lazy[idx + 3] = a * self._lazy[idx + 3] + b
    
    def _build(self, idx):
        """make the changes to idx be known to its ancestors"""
        idx >>= 1
        while idx:
            # TODO
            self.data[idx] = self.data[2 * idx] + self.data[2 * idx + 1]
            idx >>= 1
 
    def _update(self, idx):
        """updates the node idx to know of all queries applied to it via its ancestors"""
        for i in reversed(range(1, idx.bit_length())):
            self._push(idx >> i)
 
    def add(self, start, stop, ab):
        """lazily add value to [start, stop)"""
        a, b = ab
        start = start_copy = start + self._size
        stop = stop_copy = stop + self._size
 
        # Apply all the lazily stored queries
        self._update(start); self._update(stop - 1)
 
        while start < stop:
            if start & 1:
                self.data[start] = a * self.data[start] + b
                self._lazy[2 * start] = a * self._lazy[2 * start]
                self._lazy[2 * start + 1] = a * self._lazy[2 * start + 1] + b
                start += 1
            if stop & 1:
                stop -= 1
                self.data[stop] = a * self.data[stop] + b
                self._lazy[2 * stop] = a * self._lazy[2 * stop]
                self._lazy[2 * stop + 1] = a * self._lazy[2 * stop + 1] + b
            start >>= 1; stop >>= 1; b <<= 1
        
        while not start_copy&1: start_copy >>= 1
        while not stop_copy&1: stop_copy >>= 1
        self._build(start_copy); self._build(stop_copy - 1)
 
    def query(self, start, stop, res = 0):
        """func of data[start, stop)"""
        start += self._size; stop += self._size
 
        # Apply all the lazily stored queries
        self._update(start); self._update(stop - 1)
        while start < stop:
            if start & 1:
                res += self.data[start]
                start += 1
            if stop & 1:
                stop -= 1
                res += self.data[stop]
            start >>= 1; stop >>= 1
        return res
 
def main():
    n, q = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    seg = LazySegmentTree(arr)

    for _ in range(q):
        t, a, b, *x = map(int, input().split())
        if t == 1:
            seg.add(a-1, b, (1, x[0]))
        elif t == 2:
            seg.add(a-1, b, (0, x[0]))
        else:
            print(seg.query(a-1, b))
























# class SegmentTree:
#     def __init__(self, n, e, arr=None):
#         self.n = n
#         self.log = (n-1).bit_length()
#         self.size = 1<<self.log       
#         self.e = e
#         self.data = [e] * (self.size<<1)
#         self.len = [1] * (self.size<<1)        
#         if arr: self.build(arr)
            
#     def _update(self, i): self.data[i] = op(self.data[i<<1], self.data[i<<1|1])
    
#     def build(self, data):
#         """Builds the segment tree [Called Automatically upon __init__]. O(n)"""
#         for i, a in enumerate(data, self.size): self.data[i] = a
#         for i in range(self.size-1, 0, -1):
#             self._update(i)
#             self.len[i] = self.len[i<<1] + self.len[i<<1|1]
    
#     def update(self, k, x):
#         """Updates the k-th element (0-indexed) to x. O(log n)"""
#         k += self.size
#         self.data[k] = x
#         for i in range(1, self.log+1): self._update(k>>i)
#     def __setitem__(self, k, x):
#         k += self.size
#         self.data[k] = x
#         for i in range(1, self.log+1): self._update(k>>i)
            
#     def add(self, k, x):
#         """Adds x to the k-th element (0-indexed). O(log n)"""
#         k += self.size
#         self.data[k] += x
#         for i in range(1, self.log+1): self._update(k>>i)
#     def __iadd__(self, k, x):
#         k += self.size
#         self.data[k] += x
#         for i in range(1, self.log+1): self._update(k>>i)

#     def get(self, k):
#         """Returns the k-th element (0-indexed). O(1)"""
#         return self.data[k+self.size]
#     def __getitem__(self, k):
#         return self.data[k+self.size]
    
#     def query(self, l, r):
#         """Returns op(a[l], ..., a[r-1]). O(log n)"""
#         sml, smr = self.e, self.e
#         l += self.size
#         r += self.size
#         while l < r:
#             if l&1:
#                 sml = op(sml, self.data[l])
#                 l += 1
#             if r&1:
#                 r -= 1
#                 smr = op(self.data[r], smr)
#             l >>= 1
#             r >>= 1
#         return op(sml, smr)
    
#     def query_all(self):
#         """Returns op(a[0], ..., a[n-1]). O(1)"""
#         return self.data[1]
    
#     def __repr__(self) -> str:
#         return f"STree({[self[i] for i in range(self.n)]})"
# """
# Usage of SegmentTree(n, e, arr):
#     op is a binary operation on S, e.g. op = lambda x, y: x + y
#     N is the length of the array, e.g. N = 10
#     e is the identity element of op, e.g. e = 0
#     A is the initial array, e.g. A = [1] * N
# """
# # def op(x, y):
# # e = 
# # seg = SegmentTree(N, e, A)


# class LazySegmentTree(SegmentTree):
#     def __init__(self, n, e, id_, arr=None):
#         super().__init__(n, e, arr)   # builds LazySegmentTree
#         self.id = id_
#         self.lazy = [id_] * self.size
        
#     def _all_apply(self, i, F):
#         self.data[i] = mapping(F, self.data[i], self.len[i])
#         if i < self.size: self.lazy[i] = composition(F, self.lazy[i])
    
#     def _push(self, i):
#         self._all_apply(i<<1, self.lazy[i])
#         self._all_apply(i<<1|1, self.lazy[i])
#         self.lazy[i] = self.id
    
#     def update(self, k, x):
#         """Updates the k-th element (0-indexed) to x. O(log n)"""
#         k += self.size
#         for i in range(self.log, 0, -1): self._push(k>>i)
#         self.data[k] = x
#         for i in range(1, self.log+1): self._update(k>>i)
#     def __setitem__(self, k, x):
#         k += self.size
#         for i in range(self.log, 0, -1): self._push(k>>i)
#         self.data[k] = x
#         for i in range(1, self.log+1): self._update(k>>i)
            
#     def apply(self, k, F):
#         """Applies F to the k-th element (0-indexed). O(log n)"""
#         k += self.size
#         for i in range(self.log, 0, -1): self._push(k>>i)
#         self.data[k] = mapping(F, self.data[k], self.len[k])
#         for i in range(1, self.log+1): self._update(k>>i)
    
#     def range_apply(self, l, r, F):
#         """Applies F to the elements in [l, r) (0-indexed). O(log n)
#         Here F is not a lambda function, but an encoded value which is
#         passed to the mapping and composition functions."""
#         if l == r: return
#         l += self.size
#         r += self.size
#         for i in range(self.log, 0, -1):
#             if ((l>>i)<<i) != l: self._push(l>>i)
#             if ((r>>i)<<i) != r: self._push((r-1)>>i)
#         l2, r2 = l, r
#         while l < r:
#             if l&1:
#                 self._all_apply(l, F)
#                 l += 1
#             if r&1:
#                 r -= 1
#                 self._all_apply(r, F)
#             l >>= 1
#             r >>= 1
#         l, r = l2, r2
#         for i in range(1, self.log+1):
#             if ((l>>i)<<i) != l: self._update(l>>i)
#             if ((r>>i)<<i) != r: self._update((r-1)>>i)
        
#     def range_update(self, l, r, x):
#         """Assigns x to the elements in [l, r) (0-indexed). O(log n)"""
#         self.range_apply(l, r, encode(0, x))

#     def range_add(self, l, r, x):
#         """Adds x to the elements in [l, r) (0-indexed). O(log n)"""
#         self.range_apply(l, r, encode(1, x))

                
#     def get(self, k):
#         """Returns the k-th element (0-indexed). O(log n)"""
#         k += self.size
#         for i in range(self.log, 0, -1): self._push(k>>i)
#         return self.data[k]
#     def __getitem__(self, k):
#         k += self.size
#         for i in range(self.log, 0, -1): self._push(k>>i)
#         return self.data[k]
    
#     def query(self, l, r):
#         """Returns op(a[l], ..., a[r-1]). O(log n)"""
#         if l == r: return self.e
#         l += self.size
#         r += self.size
#         for i in range(self.log, 0, -1):
#             if ((l>>i)<<i) != l: self._push(l>>i)
#             if ((r>>i)<<i) != r: self._push((r-1)>>i)   
#         sml, smr = self.e, self.e
#         while l < r:
#             if l&1:
#                 sml = op(sml, self.data[l])
#                 l += 1
#             if r&1:
#                 r -= 1
#                 smr = op(self.data[r], smr)
#             l >>= 1
#             r >>= 1
#         return op(sml, smr)

#     def max_right(self, l, func):
#         """Returns r s.t. func(op(a[l], ..., a[r-1])) holds. O(log n)"""
#         if l == self.n: return self.n
#         l += self.size
#         for i in range(self.log, 0, -1): self._push(l>>i)
#         sm = self.e
#         while 1:
#             while not l&1: l >>= 1
#             if not func(op(sm, self.data[l])):
#                 while l < self.size:
#                     self._push(l)
#                     l <<= 1
#                     if func(op(sm, self.data[l])):
#                         sm = op(sm, self.data[l])
#                         l += 1
#                 return l - self.size
#             sm = op(sm, self.data[l])
#             l += 1
#             if (l&-l) == l: break
#         return self.n
    
#     def max_left(self, r, func):
#         """Returns l s.t. func(op(a[l], ..., a[r-1])) holds. O(log n)"""
#         if r == 0: return 0
#         r += self.size
#         for i in range(self.log, 0, -1): self._push((r-1)>>i)
#         sm = self.e
#         while 1:
#             r -= 1
#             while r>1 and r&1: r >>= 1
#             if not func(op(self.data[r], sm)):
#                 while r < self.size:
#                     self._push(r)
#                     r = r<<1|1
#                     if func(op(self.data[r], sm)):
#                         sm = op(self.data[r], sm)
#                         r -= 1
#                 return r+1 - self.size
#             sm = op(self.data[r], sm)
#             if (r&-r) == r: break
#         return 0
# """
# Usage of LazySegmentTree(n, e, id_, A):
#     N is the size of the array.
#     e is the identity element of op.
#     id_ is the identity element of mapping.
#     A is the initial array.
#     op is a binary operation. op(a, e) = op(e, a) = a.
#     op must be associative. op(a, op(b, c)) = op(op(a, b), c).
# """
# #def op(x, y):
# #e =
# #def composition(f, g):
# #id_ =
# #def mapping(f, x, size):
# #seg = LazySegmentTree(N, e, id_, A)


# # # Range Sum Query with Modulo
# # mask = (1<<30)-1   # 1<<30 is used because it is just greater than 1e9
# # def composition(f, g):
# #     a, b = f>>30, f&mask
# #     c, d = g>>30, g&mask
# #     e, f = a*c, a*d+b
# #     return (e%M)<<30|(f%M)
# # id_ = 1<<30     # Identity element of mapping
# # def mapping(f, x, size):
# #     a, b = f>>30, f&mask
# #     return (a*x + b*size)%M
# # def op(x, y): return (x+y)%M
# # e = 0           # Identity element of op


# # Range Sum Query without Modulo
# mask = (1<<38)-1  # 1<<30 is used because it is just greater than 1e9
# def composition(f, g):
#     a, b = f
#     c, d = g
#     e, f = a*c, a*d+b
#     return e, f
# id_ = (1, 0)     # Identity element of mapping
# def mapping(f, x, size):
#     a, b = f
#     return a*x+b*size
# def op(x, y): return x+y
# e = 0           # Identity element of op


# def encode(x, y): return (x, y)
# def decode(z): return z



# def main():
#     n, q = [int(i) for i in input().split()]
#     arr = [int(i) for i in input().split()]
#     seg = LazySegmentTree(n, e, id_, arr)

#     for _ in range(q):
#         t, a, b, *x = map(int, input().split())
#         if t == 1:
#             seg.range_add(a-1, b, x[0])
#         elif t == 2:
#             seg.range_update(a-1, b, x[0])
#         else:
#             print(seg.query(a-1, b))

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# ======================== Functions declaration Starts ========================
abc='abcdefghijklmnopqrstuvwxyz'
abd={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

def copy2d(lst): return [x[:] for x in lst]   #Copy 2D list... Avoid Using Deepcopy
def no_of_digits(num): return 0 if num <= 0 else int(log10(num)) + 1
def powm(num, power, mod=M): return pow(num, power, mod)
def isPowerOfTwo(x): return (x and (not(x & (x - 1))))
def LSB(num):
    """Returns Least Significant Bit of a number (Rightmost bit) in O(1)"""
    return num & -num

def MSB(num):
    """Returns Most Significant Bit of a number (Leftmost bit) in O(logN)"""
    if num <= 0: return 0
    ans = 1; num >>= 1
    while num:
        num >>= 1; ans <<= 1
    return ans


LB = bisect_left   # Lower bound
UB = bisect_right  # Upper bound
 
def BS(a, x):      # Binary Search
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x*y)//gcd(x,y)


# import threading
# def dmain():
#     sys.setrecursionlimit(1000000)
#     threading.stack_size(1024000)
#     thread = threading.Thread(target=main)
#     thread.start()
            
# =============================== Custom Classes ===============================

class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ R
Int = lambda x:Wrapper(int(x))        

class myDict():
    def __init__(self,func=int):
        # self.RANDOM = randint(0,1<<32)
        self.RANDOM = R
        self.default=func
        self.dict={}
    def __getitem__(self,key):
        myKey=self.RANDOM^key
        if myKey not in self.dict:
            self.dict[myKey]=self.default()
        return self.dict[myKey]
    def __setitem__(self,key,item):
        myKey=self.RANDOM^key
        self.dict[myKey]=item
    def __contains__(self,key):
        myKey=self.RANDOM^key
        return myKey in self.dict
    def __delitem__(self,key):
        myKey=self.RANDOM^key
        del self.dict[myKey]
    def keys(self):
        return [self.RANDOM^i for i in self.dict]


# =============================== Region Fastio ===============================
if not os.path.isdir('C:/users/acer'):
    BUFSIZE = 8192
    
    
    class FastIO(IOBase):
        newlines = 0
    
        def __init__(self, file):
            self._fd = file.fileno()
            self.buffer = BytesIO()
            self.writable = "x" in file.mode or "r" not in file.mode
            self.write = self.buffer.write if self.writable else None
    
        def read(self):
            while True:
                b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                if not b:
                    break
                ptr = self.buffer.tell()
                self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
            self.newlines = 0
            return self.buffer.read()
    
        def readline(self):
            while self.newlines == 0:
                b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                self.newlines = b.count(b"\n") + (not b)
                ptr = self.buffer.tell()
                self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
            self.newlines -= 1
            return self.buffer.readline()
    
        def flush(self):
            if self.writable:
                os.write(self._fd, self.buffer.getvalue())
                self.buffer.truncate(0), self.buffer.seek(0)
    
    
    class IOWrapper(IOBase):
        def __init__(self, file):
            self.buffer = FastIO(file)
            self.flush = self.buffer.flush
            self.writable = self.buffer.writable
            self.write = lambda s: self.buffer.write(s.encode("ascii"))
            self.read = lambda: self.buffer.read().decode("ascii")
            self.readline = lambda: self.buffer.readline().decode("ascii")
    
    
    def print(*args, **kwargs):
        """Prints the values to a stream, or to sys.stdout by default."""
        sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
        at_start = True
        for x in args:
            if not at_start:
                file.write(sep)
            file.write(str(x))
            at_start = False
        file.write(kwargs.pop("end", "\n"))
        if kwargs.pop("flush", False):
            file.flush()
    
    
    if sys.version_info[0] < 3:
        sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
    else:
        sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    
    input = lambda: sys.stdin.readline().rstrip("\r\n")

# =============================== Endregion ===============================

if __name__ == "__main__":
    #read()
    main()
    #dmain()
