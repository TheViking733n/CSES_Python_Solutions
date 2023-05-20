"""
[(1, 10), (2, 3), (4, 1), ]

"""

n = int(input())
a, b = [], []
for i in range(n):
    x, y = map(int, input().split())
    a.append(x); b.append(y)
a.sort(); b.sort()
ans = cnt = x = y = 0
while x < n:
    if a[x] < b[y]:
        cnt += 1
        x += 1
    else:
        cnt -= 1
        y += 1
    ans = max(ans,cnt)
print(ans)


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




