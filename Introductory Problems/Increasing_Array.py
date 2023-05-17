n, a = int(input()), list(map(int, input().split()))
ans = 0
for i in range(n-1):
    d = max(0, a[i]-a[i+1])
    a[i+1] += d
    ans += d
print(ans)