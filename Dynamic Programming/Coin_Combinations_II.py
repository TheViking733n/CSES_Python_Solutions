"""
dp[i][k]
    No. of ways to produce a sum i, using only first k coins

"""

M = 10 ** 9 + 7
# def partition_generalised(n, arr): # No. of partition of n using only arr
#     # Note: arr must be sorted
#     dp = [0] * (n + 1)
#     dp[0] = 1
#     for i in arr:
#         for j in range(i, n + 1):
#             dp[j] += dp[j - i]
#             dp[j] %= M
#     return dp[n]

n, x = map(int, input().split())
coins = sorted(map(int, input().split()))
# print(partition_generalised(x, coins))

dp = [[0] * 2 for _ in range(x + 1)]
dp[0][0] = 1
for k in range(len(coins)):
    for i in range(1, x + 1):
        if k-1 >= 0:
            dp[i][k&1] = dp[i][k-1&1]
        if i-coins[k] >= 0:
            dp[i][k&1] += dp[i-coins[k]][k&1]
        dp[i][k&1] %= M

print(sum(dp[x]) % M)