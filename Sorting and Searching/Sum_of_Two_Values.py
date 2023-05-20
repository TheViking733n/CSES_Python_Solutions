n, x = map(int, input().split())
a = list(map(int, input().split()))
ind = sorted([(a[i], i) for i in range(n)])
a.sort()
i, j = 0, n - 1
while i < j:
    if a[i] + a[j] == x:
        print(ind[i][1] + 1, ind[j][1] + 1)
        exit()
    elif a[i] + a[j] < x:
        i += 1
    else:
        j -= 1
print("IMPOSSIBLE")