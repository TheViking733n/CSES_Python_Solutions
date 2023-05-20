n, k = map(int, input().split())
arr = list(map(int, input().split()))
seen = {0}
ans = sm = 0
for i in arr:
    sm += i
    seen.add(sm)
    ans += (sm - k) in seen
print(ans)