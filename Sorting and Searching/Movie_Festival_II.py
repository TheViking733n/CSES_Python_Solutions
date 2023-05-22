import sys
from heapq import heappush, heappop
input = sys.stdin.readline

encode = lambda a, b : a << 32 | b
decode = lambda x : (x >> 32, x & 0xffffffff)

n, k = map(int, input().split())
arr = [encode(*list(map(int, input().split()))[::-1]) for _ in range(n)]
arr.sort()
member = [-1] * k
ans = 0
for i in range(n):
    en, st = decode(arr[i])
    if member[0] <= st:
        heappop(member)
        heappush(member, en)
        ans += 1
print(ans)