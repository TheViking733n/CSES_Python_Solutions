"""
Push DP solution
dp[i] = minimum no. of ways to make sum i
then for every coin in arr:
    dp[i+coin] = dp[i] + 1

Pull DP
"""

import sys
input = sys.stdin.readline
n, x = map(int, input().split())
arr = sorted(map(int, input().split()))

# # Pull DP
# dp = [1 << 31] * (x + 1)
# dp[0] = 0
# for i in range(1, x + 1):
#     for coin in arr:
#         if i - coin < 0:
#             break
#         dp[i] = min(dp[i], dp[i-coin] + 1)
# print(dp[x] if dp[x] != (1 << 31) else -1)


# # ==================================
# # Push DP
dp = [1 << 31] * (x + 1)
dp[0] = 0
for i in range(x):
    for coin in arr:
        if i+coin<x+1:
            dp[i+coin] = min(dp[i+coin], dp[i]+1)
        else: break
print(dp[x] if dp[x] != (1 << 31) else -1)
