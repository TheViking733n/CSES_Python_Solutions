"""
dp[i] represents the sum that can't be made using 
elements from index 0..i
if dp[i] == k
therefore
all numbers from 0 to k-1 are possible to make using the first i elements
if arr[i+1] = v
then new set of possible sums will be:
0, 1, .., k-1, v, v+1, .. v+k-1
now two possible cases
1. v > k, i.e. arr[i+1] > dp[i]
    The number 'k' is missing, i.e. ans = k
2. otherwise
    dp[i+1] = dp[i] + arr[i+1]
"""

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

# # DP solution:
# dp = [0] * (n + 1)
# dp[0] = 1
# for i in range(n):
#     if arr[i] > dp[i]:
#         print(dp[i])
#         exit()
#     dp[i+1] = dp[i] + arr[i]
# print(dp[n])

# DP with space optimization
ans = 1
for i in arr:
    if i > ans:
        print(ans)
        exit()
    ans += i
print(ans)