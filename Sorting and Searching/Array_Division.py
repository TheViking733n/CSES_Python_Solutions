n, k = map(int, input().split())
arr = list(map(int, input().split()))
low = 0
high = sum(arr)
ans = high
while low <= high:
    mid = low + high >> 1
    maxsum = sm = 0; cnt = 1
    for i in range(n):
        if sm + arr[i] <= mid:
            sm += arr[i]
            maxsum = max(maxsum, sm)
        else:
            sm = arr[i]
            maxsum = max(maxsum, sm)
            if sm > mid:  # Not possible with this mid, increase low
                cnt = k + 1
                maxsum = 99   # Inf
                break
            cnt += 1
    # print(low, high, '\t|', mid, '\t|', maxsum, sm, '\t|', cnt, ans)
    if cnt > k:
        low = mid + 1
    else:
        ans = min(ans, maxsum)
        high = mid - 1
print(ans)