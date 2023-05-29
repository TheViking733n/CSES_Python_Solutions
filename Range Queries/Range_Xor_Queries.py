from itertools import accumulate
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
a = [0] + list(accumulate(map(int, input().split()), lambda x, y: x ^ y))
for _ in range(q):
    l, r = map(int, input().split())
    print(a[r] ^ a[l - 1])