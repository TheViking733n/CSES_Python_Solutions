class SortedList:
    def __init__(self, iterable=[], _load=200):
        """Initialize sorted list instance."""
        values = sorted(iterable)
        self._len = _len = len(values)
        self._load = _load
        self._lists = _lists = [values[i:i + _load] for i in range(0, _len, _load)]
        self._list_lens = [len(_list) for _list in _lists]
        self._mins = [_list[0] for _list in _lists]
        self._fen_tree = []
        self._rebuild = True

    def _fen_build(self):
        """Build a fenwick tree instance."""
        self._fen_tree[:] = self._list_lens
        _fen_tree = self._fen_tree
        for i in range(len(_fen_tree)):
            if i | i + 1 < len(_fen_tree):
                _fen_tree[i | i + 1] += _fen_tree[i]
        self._rebuild = False

    def _fen_update(self, index, value):
        """Update `fen_tree[index] += value`."""
        if not self._rebuild:
            _fen_tree = self._fen_tree
            while index < len(_fen_tree):
                _fen_tree[index] += value
                index |= index + 1

    def _fen_query(self, end):
        """Return `sum(_fen_tree[:end])`."""
        if self._rebuild:
            self._fen_build()

        _fen_tree = self._fen_tree
        x = 0
        while end:
            x += _fen_tree[end - 1]
            end &= end - 1
        return x

    def _fen_findkth(self, k):
        """Return a pair of (the largest `idx` such that `sum(_fen_tree[:idx]) <= k`, `k - sum(_fen_tree[:idx])`)."""
        _list_lens = self._list_lens
        if k < _list_lens[0]:
            return 0, k
        if k >= self._len - _list_lens[-1]:
            return len(_list_lens) - 1, k + _list_lens[-1] - self._len
        if self._rebuild:
            self._fen_build()

        _fen_tree = self._fen_tree
        idx = -1
        for d in reversed(range(len(_fen_tree).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(_fen_tree) and k >= _fen_tree[right_idx]:
                idx = right_idx
                k -= _fen_tree[idx]
        return idx + 1, k

    def _delete(self, pos, idx):
        """Delete value at the given `(pos, idx)`."""
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens

        self._len -= 1
        self._fen_update(pos, -1)
        del _lists[pos][idx]
        _list_lens[pos] -= 1

        if _list_lens[pos]:
            _mins[pos] = _lists[pos][0]
        else:
            del _lists[pos]
            del _list_lens[pos]
            del _mins[pos]
            self._rebuild = True

    def _loc_left(self, value):
        """Return an index pair that corresponds to the first position of `value` in the sorted list."""
        if not self._len:
            return 0, 0

        _lists = self._lists
        _mins = self._mins

        lo, pos = -1, len(_lists) - 1
        while lo + 1 < pos:
            mi = (lo + pos) >> 1
            if value <= _mins[mi]:
                pos = mi
            else:
                lo = mi

        if pos and value <= _lists[pos - 1][-1]:
            pos -= 1

        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value <= _list[mi]:
                idx = mi
            else:
                lo = mi

        return pos, idx

    def _loc_right(self, value):
        """Return an index pair that corresponds to the last position of `value` in the sorted list."""
        if not self._len:
            return 0, 0

        _lists = self._lists
        _mins = self._mins

        pos, hi = 0, len(_lists)
        while pos + 1 < hi:
            mi = (pos + hi) >> 1
            if value < _mins[mi]:
                hi = mi
            else:
                pos = mi

        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value < _list[mi]:
                idx = mi
            else:
                lo = mi

        return pos, idx

    def add(self, value):
        """Add `value` to sorted list."""
        _load = self._load
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens

        self._len += 1
        if _lists:
            pos, idx = self._loc_right(value)
            self._fen_update(pos, 1)
            _list = _lists[pos]
            _list.insert(idx, value)
            _list_lens[pos] += 1
            _mins[pos] = _list[0]
            if _load + _load < len(_list):
                _lists.insert(pos + 1, _list[_load:])
                _list_lens.insert(pos + 1, len(_list) - _load)
                _mins.insert(pos + 1, _list[_load])
                _list_lens[pos] = _load
                del _list[_load:]
                self._rebuild = True
        else:
            _lists.append([value])
            _mins.append(value)
            _list_lens.append(1)
            self._rebuild = True

    def discard(self, value):
        """Remove `value` from sorted list if it is a member."""
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_right(value)
            if idx and _lists[pos][idx - 1] == value:
                self._delete(pos, idx - 1)

    def remove(self, value):
        """Remove `value` from sorted list; `value` must be a member."""
        _len = self._len
        self.discard(value)
        if _len == self._len:
            raise ValueError('{0!r} not in list'.format(value))

    def pop(self, index=-1):
        """Remove and return value at `index` in sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        value = self._lists[pos][idx]
        self._delete(pos, idx)
        return value

    def bisect_left(self, value):
        """Return the first index to insert `value` in the sorted list."""
        pos, idx = self._loc_left(value)
        return self._fen_query(pos) + idx

    def bisect_right(self, value):
        """Return the last index to insert `value` in the sorted list."""
        pos, idx = self._loc_right(value)
        return self._fen_query(pos) + idx

    def count(self, value):
        """Return number of occurrences of `value` in the sorted list."""
        return self.bisect_right(value) - self.bisect_left(value)

    def __len__(self):
        """Return the size of the sorted list."""
        return self._len

    def __getitem__(self, index):
        """Lookup value at `index` in sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        return self._lists[pos][idx]

    def __delitem__(self, index):
        """Remove value at `index` from sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        self._delete(pos, idx)

    def __contains__(self, value):
        """Return true if `value` is an element of the sorted list."""
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_left(value)
            return idx < len(_lists[pos]) and _lists[pos][idx] == value
        return False

    def __iter__(self):
        """Return an iterator over the sorted list."""
        return (value for _list in self._lists for value in _list)

    def __reversed__(self):
        """Return a reverse iterator over the sorted list."""
        return (value for _list in reversed(self._lists) for value in reversed(_list))

    def __repr__(self):
        """Return string representation of sorted list."""
        return 'SortedList({0})'.format(list(self))



n, k = map(int, input().split())
arr = [int(i) for i in input().split()]

s = SortedList(arr[:k])
ans = [s[k - 1 >> 1]]

for i in range(k, n):
    s.add(arr[i])
    s.remove(arr[i - k])
    ans.append(s[k - 1 >> 1])
print(*ans)


















# import random
# from collections import defaultdict, deque
# from heapq import heappush, heappop

# class DefaultDict:
#     def __init__(self, default=None):
#         self.default = default
#         self.x = random.randrange(1, 1 << 31)
#         self.dd = defaultdict(default)
 
#     def __repr__(self):
#         return "{"+", ".join(f"{k ^ self.x}: {v}" for k, v in self.dd.items())+"}"
 
#     def __eq__(self, other):
#         return set(self.dd.items()) == set(other.dd.items())
 
#     def __or__(self, other):
#         res = DefaultDict(self.default)
#         for k, v in self.dd: res[k] = v
#         for k, v in other.dd: res[k] = v
#         return res
 
#     def __len__(self):
#         return len(self.dd)
 
#     def __getitem__(self, item):
#         return self.dd[item ^ self.x]
 
#     def __setitem__(self, key, value):
#         self.dd[key ^ self.x] = value
 
#     def __delitem__(self, key):
#         del self.dd[key ^ self.x]
 
#     def __contains__(self, item):
#         return item ^ self.x in self.dd
 
#     def items(self):
#         for k, v in self.dd.items(): yield (k ^ self.x, v)
 
#     def keys(self):
#         for k in self.dd: yield k ^ self.x
 
#     def values(self):
#         for v in self.dd.values(): yield v
 
#     def __iter__(self):
#         for k in self.dd: yield k ^ self.x

# class DeletableMinHeapQ():
#     def __init__(self):
#         self.H = []
#         self.HC = DefaultDict(int)
#         self.size = 0
#     def hpush(self, x):
#         heappush(self.H, x)
#         self.HC[x] += 1
#         self.size += 1
#     def hpop(self):
#         t = heappop(self.H)
#         while not self.HC[t]:
#             t = heappop(self.H)
#         self.HC[t] -= 1
#         self.size -= 1
#         return t
#     def hmin(self):
#         t = self.H[0]
#         while not self.HC[t]:
#             heappop(self.H)
#             t = self.H[0]
#         return t
#     def __len__(self):
#         return self.size
#     def __getitem__(self, i):
#         return self.H[i]
#     def getMin(self):
#         return self.H[0]
#     def hdel(self, x):
#         if self.HC[x] > 0:
#             self.HC[x] -= 1
#             self.size -= 1
#             return True
#         return False

# class MedianPQ:
#     def __init__(self, n):
#         self.n = n
#         self.left = DeletableMinHeapQ()
#         self.right = DeletableMinHeapQ()
#         self.q = deque()
    
#     def push(self, x):
#         n, left, right = self.n, self.left, self.right
#         left.hpush(-x)
#         self.q.append(x)
#         if len(self.q) > n:
#             v = self.q.popleft()
#             left.hdel(-v) or right.hdel(v)

#         if len(left) > len(right) + 1:
#             v = -left.hpop()
#             right.hpush(v)
#         elif len(left) < len(right):
#             v = right.hpop()
#             left.hpush(v)
    
#     def median(self):
#         v = -self.left.hmin()
#         # self.left.hpush(-v)
#         return v




# n, k = map(int, input().split())
# arr = [int(i) for i in input().split()]
# ans = []
# pq = MedianPQ(k)
# for i in range(k-1):
#     pq.push(arr[i])

# for i in range(k-1, n):
#     pq.push(arr[i])
#     ans.append(pq.median())

# print(ans)


