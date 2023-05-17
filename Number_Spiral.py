n = int(input())
for _ in range(n):
    i, j = list(map(int, input().split()))
    x = max(i, j)
    d = x*x + (x-1)*(x-1) + 1 >> 1
    print(d + [-1, 1][(x & 1) ^ (i > j)] * abs(i-j))
