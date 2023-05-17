from itertools import combinations
n = int(input())
arr = list(map(int, input().split()))
ans = tot = sum(arr)
for take in range(1, n):
    for comb in combinations(arr, take):
        firstGroup = sum(comb)
        secondGroup = tot - firstGroup
        ans = min(ans, abs(firstGroup - secondGroup))
print(ans)