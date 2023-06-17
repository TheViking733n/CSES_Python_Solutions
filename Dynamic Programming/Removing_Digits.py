import sys
n = int(sys.stdin.readline())
dp = [1 << 20] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    for dig in str(i):
        dp[i] = min(dp[i], dp[i - int(dig)] + 1)
print(dp[n])