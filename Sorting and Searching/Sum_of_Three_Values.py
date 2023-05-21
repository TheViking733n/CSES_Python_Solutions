n, tar = map(int, input().split())
arr = list(map(int, input().split()))
a2 = [(arr[i], i) for i in range(n)]
a2.sort()
ind = []
for i in range(n):
    v, idx = a2[i]
    arr[i] = v
    ind.append(idx + 1)
possible = False
for j in range(1, n-1):
    i, k = 0, n - 1
    while i < k:
        s = arr[i] + arr[j] + arr[k]
        if i == j:
            i += 1
            continue
        if k == j:
            k -= 1
            continue
        if s == tar:
            possible = True
            break
        elif s < tar:
            i += 1
        else:
            k -= 1
    
    if possible:
        print(ind[i], ind[j], ind[k])
        exit()

print("IMPOSSIBLE")
        
