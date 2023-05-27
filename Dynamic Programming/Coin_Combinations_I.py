# a,b=map(int,input().split())
# c=[*map(int,input().split())]
# d=[1]+[0]*(b)
# for x in range(b+1):
#  for e in c:
#    if x+e<=b:
#     d[x+e]=(d[x]+d[x+e])%(10**9 + 7)
# print(d[b])

from sys import stdin
M = 10 ** 9 + 7
n, x = map(int, stdin.readline().split())
arr = sorted(map(int, stdin.readline().split()))
dp = [0] * (x + 1); dp[0] = 1
for i in range(1, x+1):
    for coin in arr:
        if i - coin < 0: break
        dp[i] = (dp[i] + dp[i-coin]) % M
print(dp[x])