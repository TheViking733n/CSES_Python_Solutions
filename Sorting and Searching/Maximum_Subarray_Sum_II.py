"""
0 1 2 3 4 5 6 7 8 9
      3 2 1 0                 
_ _ _ _ _ _ _ _ _ _ _ _
[ x ]       i

for every i, find let x be an index behind i
then size of this subarray = i - x + 1
min size = a => x = i - a + 1
max size = b => x = i - b + 1
prefix sum of subarray [x, i] = ps[i+1] - ps[x]
maximum value of this quantity for some fixed 'i' :
    
"""
import random
from collections import defaultdict
from heapq import heappush, heappop

class DefaultDict:
    def __init__(self, default=None):
        self.default = default
        self.x = random.randrange(1, 1 << 31)
        self.dd = defaultdict(default)
 
    def __repr__(self):
        return "{"+", ".join(f"{k ^ self.x}: {v}" for k, v in self.dd.items())+"}"
 
    def __eq__(self, other):
        return set(self.dd.items()) == set(other.dd.items())
 
    def __or__(self, other):
        res = DefaultDict(self.default)
        for k, v in self.dd: res[k] = v
        for k, v in other.dd: res[k] = v
        return res
 
    def __len__(self):
        return len(self.dd)
 
    def __getitem__(self, item):
        return self.dd[item ^ self.x]
 
    def __setitem__(self, key, value):
        self.dd[key ^ self.x] = value
 
    def __delitem__(self, key):
        del self.dd[key ^ self.x]
 
    def __contains__(self, item):
        return item ^ self.x in self.dd
 
    def items(self):
        for k, v in self.dd.items(): yield (k ^ self.x, v)
 
    def keys(self):
        for k in self.dd: yield k ^ self.x
 
    def values(self):
        for v in self.dd.values(): yield v
 
    def __iter__(self):
        for k in self.dd: yield k ^ self.x

class DeletableMinHeapQ():
    def __init__(self):
        self.H = []
        self.HC = DefaultDict(int)
    def hpush(self, x):
        heappush(self.H, x)
        self.HC[x] += 1
    def hpop(self):
        t = heappop(self.H)
        while not self.HC[t]:
            t = heappop(self.H)
        self.HC[t] -= 1
        return t
    def hmin(self):
        t = self.H[0]
        while not self.HC[t]:
            heappop(self.H)
            t = self.H[0]
        return t
    def hdel(self, x):
        if self.HC[x] > 0:
            self.HC[x] -= 1

n, a, b = map(int, input().split())
arr = [int(i) for i in input().split()]
b += 1
st = DeletableMinHeapQ()
# st.hpush(0)
ps = [0]
for i in arr: ps.append(ps[-1] + i)
# ps.pop(0)
ans = ps[a]

for i in range(a-1, n):
    i1, i2 = i - b + 1, i - a + 1
    st.hpush(ps[i2])
    # print(arr[max(0,i1):i2+1], i)
    if i1 >= 0: st.hdel(ps[i1])
    ans = max(ans, ps[i+1] - st.hmin())
print(ans)
    
