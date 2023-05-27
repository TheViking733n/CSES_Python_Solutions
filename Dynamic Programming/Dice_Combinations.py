"""
Recurrence: f(n) = f(n-1) + f(n-2) + f(n-3) + f(n-4) + f(n-5) + f(n-6)

"""

M = 10 ** 9 + 7
n = int(input())
dp = [0] * (n + 6)
dp[0] = 1
for i in range(n):
    for j in range(1, 7):
        dp[i+j] += dp[i]
        dp[i+j] %= M
print(dp[n])