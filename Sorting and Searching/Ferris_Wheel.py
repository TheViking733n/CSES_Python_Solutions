n, x = map(int, input().split())
a = sorted(map(int, input().split()))
ans, i, j = 0, 0, n - 1
while i < j:
    i += a[i] + a[j] <= x
    ans += 1
    j -= 1
print(ans + (i == j))