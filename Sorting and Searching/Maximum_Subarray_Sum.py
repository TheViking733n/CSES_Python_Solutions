def kadane(n, arr):
    ans = mx = arr[0]
    for i in range(1, n):
        mx = max(arr[i], mx + arr[i])
        ans = max(mx, ans)
    return ans

print(kadane(int(input()), list(map(int, input().split()))))

