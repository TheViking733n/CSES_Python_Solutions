n = int(input())
a = list(map(int, input().split()))

i = j = 0
ans = cur = 0
seen = set()

while j < n:
    if a[j] not in seen:
        seen.add(a[j])
        cur = j - i + 1
        ans = max(ans, cur)
        j += 1
    else:
        seen.remove(a[i])
        i += 1

print(ans)