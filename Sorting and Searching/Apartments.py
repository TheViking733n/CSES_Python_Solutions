n, m, k = map(int, input().split())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))
ans = i = j = 0
while i < n and j < m:
    if a[i] + k < b[j]:
        i += 1
    elif a[i] - k > b[j]:
        j += 1
    else:
        i += 1
        j += 1
        ans += 1
print(ans)
