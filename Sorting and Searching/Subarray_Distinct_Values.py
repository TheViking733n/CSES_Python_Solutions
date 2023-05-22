"""
i | j |
0   0   []
0   1   [1]
0   2   [1, 2]



"""


n, k = map(int, input().split())
arr = input().split()

box = set()

ans = i = j = 0
while i < n and j < n:
    while j < n:
        box.add(arr[j])
        j += 1
        if len(box) == k + 1:
            box.remove(arr[j-1])
            break
        # print([i, j], [int(i) for i in box])
        ans += j - i
    while i < j and len(box) >= k:
        if arr[i] in box: box.remove(arr[i])
        i += 1
    # print(i, j)

print(ans)
