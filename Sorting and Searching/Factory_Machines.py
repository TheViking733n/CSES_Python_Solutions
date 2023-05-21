n, produce = map(int, input().split())
arr = [int(i) for i in input().split()]
l, h = 0, int(1e18)
ans = h
while l <= h:
    mid = l + h >> 1
    made = 0
    for i in arr:
        made += mid // i
    if made >= produce:
        h = mid - 1
        ans = min(ans, mid)
    else:
        l = mid + 1
print(ans)
