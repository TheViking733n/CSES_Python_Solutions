import sys
input = sys.stdin.readline
n = int(input())
M = 10 ** 9 + 7
g = [input() for _ in range(n)]
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[1][1] = int(g[0][0] == '.')
for i in range(n):
    for j in range(n):
        if g[i][j] == '.':
            dp[i + 1][j + 1] += dp[i][j + 1] + dp[i + 1][j]
            dp[i + 1][j + 1] %= M
print(dp[n][n])