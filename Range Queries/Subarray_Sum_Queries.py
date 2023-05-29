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


def main():
    import sys
    from math import log2, ceil

    n, q = [int(s) for s in sys.stdin.readline().split()]
    n = 2 ** ceil(log2(n))
    arr = [int(s) for s in sys.stdin.readline().split()]
    
    sum_ = [0] * 2 * n
    prefix_ = [0] * 2 * n
    suffix_ = [0] * 2 * n
    subsum_ = [0] * 2 * n
    
    
    def build():
        for i, a in enumerate(arr):
            sum_[n + i] = a
            prefix_[n + i] = a if a > 0 else 0
            suffix_[n + i] = a if a > 0 else 0
            subsum_[n + i] = a
        a = n >> 1
        b = n
        while a:
            for i in range(a, b):
                sum_[i] = sum_[i << 1] + sum_[i << 1 | 1]
                prefix_[i] = max(prefix_[i << 1], sum_[i << 1] + prefix_[i << 1 | 1])
                suffix_[i] = max(suffix_[i << 1 | 1], suffix_[i << 1] + sum_[i << 1 | 1])
                subsum_[i] = max(subsum_[i << 1], subsum_[i << 1 | 1], suffix_[i << 1] + prefix_[i << 1 | 1])
            a >>= 1
            b >>= 1
    
    
    def update(k, x):
        k += n
        sum_[k] = x
        prefix_[k] = x if x > 0 else 0
        suffix_[k] = x if x > 0 else 0
        subsum_[k] = x
        while k > 1:
            k >>= 1
            sum_[k] = sum_[k << 1] + sum_[k << 1 | 1]
            prefix_[k] = max(prefix_[k << 1], sum_[k << 1] + prefix_[k << 1 | 1])
            suffix_[k] = max(suffix_[k << 1 | 1], suffix_[k << 1] + sum_[k << 1 | 1])
            subsum_[k] = max(subsum_[k << 1], subsum_[k << 1 | 1], suffix_[k << 1] + prefix_[k << 1 | 1])
    
    
    build()
    
    ans = []
    for _ in range(q):
        k, x = [int(s) for s in sys.stdin.readline().split()]
        update(k - 1, x)
        ans.append(subsum_[1])
    
    print('\n'.join((str(s) for s in ans)))

























# class Node:
#     def __init__(self, mx, pre, suf, sm):
#         self.mx = mx
#         self.pre = pre
#         self.suf = suf
#         self.sm = sm
#     def __repr__(self):
#         return f"Node({self.mx}, {self.pre}, {self.suf}, {self.sm})"
 
# def segfunc(n1, n2):
#     mx = max(n1.mx, n2.mx, n1.suf + n2.pre)
#     pre = max(n1.pre, n1.sm + n2.pre)
#     suf = max(n2.suf, n1.suf + n2.sm)
#     sm = n1.sm + n2.sm
#     return Node(mx, pre, suf, sm)
 
# class SegmentTree:
#     def __init__(self, data, default=Node(0, 0, 0, 0), func=segfunc):
#         """initialize the segment tree with data"""
#         self._default = default
#         self._func = func
#         self._len = len(data)
#         self._size = _size = 1 << (self._len - 1).bit_length()
 
#         self.data = [default] * (2 * _size)
#         self.data[_size:_size + self._len] = data
#         for i in reversed(range(_size)):
#             self.data[i] = func(self.data[i + i], self.data[i + i + 1])
 
#     def __delitem__(self, idx):
#         self[idx] = self._default
 
#     def __getitem__(self, idx):
#         return self.data[idx + self._size]
 
#     def __setitem__(self, idx, value):
#         idx += self._size
#         self.data[idx] = value
#         idx >>= 1
#         while idx:
#             self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
#             idx >>= 1
 
#     def __len__(self):
#         return self._len
 
#     def query(self, start, stop):
#         """func of data[start, stop)"""
#         start += self._size
#         stop += self._size
 
#         res_left = res_right = self._default
#         while start < stop:
#             if start & 1:
#                 res_left = self._func(res_left, self.data[start])
#                 start += 1
#             if stop & 1:
#                 stop -= 1
#                 res_right = self._func(self.data[stop], res_right)
#             start >>= 1
#             stop >>= 1
 
#         return self._func(res_left, res_right)
 
#     def __repr__(self):
#         return "SegmentTree({0})".format(self.data)
 
 

# def main():
#     n, q = [int(i) for i in input().split()]
#     arr = [int(i) for i in input().split()]
#     seg = SegmentTree([Node(i, i, i, i) for i in arr])
#     for _ in range(q):
#         k, x = map(int, input().split())
#         seg[k-1] = Node(x, x, x, x)
#         print(seg.query(0, n).mx)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
