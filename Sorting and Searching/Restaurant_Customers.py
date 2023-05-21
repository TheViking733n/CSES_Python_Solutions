"""
[(1, 10), (2, 3), (4, 1), ]
"""
def encode(st, en): return st << 32 | en
def decode(x): return x >> 32, x & 0xffffffff


import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n = int(input())
arr = [encode(*list(map(int, input().split()))) for _ in range(n)]
arr.sort()
ans = cnt = 0
pq = []
for x in arr: # Iterate through all customers in increasing time of their arrival
    st, en = decode(x)
    # Remove all the customers who already left before comming of current customer
    while pq and pq[0] < st: # pq[0] is the leaving time of the customer who is currently present in the restaurent and have smallest leaving time
        heappop(pq)
        cnt -= 1

    heappush(pq, en) # Push the leaving time of current customer in the PQ
    cnt += 1         # Increment the counter
    ans = max(ans, cnt)
print(ans)











# ===============================================
# # Two pointer approach
# n = int(input())
# a, b = [], []
# for i in range(n):
#     x, y = map(int, input().split())
#     a.append(x); b.append(y)
# a.sort(); b.sort()
# ans = cnt = x = y = 0
# while x < n:
#     if a[x] < b[y]:
#         cnt += 1
#         x += 1
#     else:
#         cnt -= 1
#         y += 1
#     ans = max(ans,cnt)
# print(ans)




# ============================================
# # Coordinates compression approach
# import sys
# from random import randint
# R = randint(1, 1 << 30)
# input = sys.stdin.readline
# n = int(input())
# pairs = [tuple(map(int, input().split())) for _ in range(n)]
# # pairs.sort()
# fInv = [i[0] for i in pairs]
# fInv.extend([i[1]+1 for i in pairs])
# fInv.sort()
# f = {}
# for i in range(len(fInv)):
#     f[R^(fInv[i])] = i
# time = [0] * (2 * n + 1)
# for u, v in pairs:
#     time[f[R^(u)]] += 1
#     time[f[R^(v+1)]] -= 1
# cnt = 0
# mx = 1
# for i in range(len(time)):
#     cnt += time[i]
#     mx = max(mx, cnt)
# print(mx[0])




