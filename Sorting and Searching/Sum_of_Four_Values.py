"""
O(N^2 LogN) solution

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
[possible sums]   ^ [----v----]
using 2 elements  i      j (loop j for every element toward right)

"""

n, tar = map(int, input().split())
arr = list(map(int, input().split()))
arr = [(arr[i], i+1) for i in range(n)]
arr.sort(key=lambda x: x[0])

possible = {}
for i in range(n):
    for j in range(i+1, n):
        req = tar - arr[i][0] - arr[j][0]
        if req in possible:
            i1, i2 = possible[req]
            print(arr[i1][1], arr[i2][1], arr[i][1], arr[j][1])
            exit()
    
    cur = arr[i][0]
    for k in range(i):
        new = cur + arr[k][0]
        if new not in possible:
            possible[new] = (k, i)

print("IMPOSSIBLE")