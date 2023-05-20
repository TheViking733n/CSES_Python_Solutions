'''
5 3 2 1 4
'''

n = int(input())
a = [int(x) - 1 for x in input().split()]
ind = [0] * n
for i in range(n):
    ind[a[i]] = i
ans = 1
for i in range(1, n):
    if ind[i] < ind[i - 1]:
        ans += 1
print(ans)