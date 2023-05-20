from collections import defaultdict
n, k = map(int, input().split())
arr = list(map(int, input().split()))
seen = defaultdict(int)
seen['0'] += 1
ans = sm = 0
for i in arr:
    sm += i
    ans += seen[str(sm - k)]
    seen[str(sm)] += 1
print(ans)