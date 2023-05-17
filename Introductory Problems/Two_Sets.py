m = n = int(input())
sm = n * (n + 1) >> 1
if sm & 1:
    print('NO')
else:
    sm >>= 1
    ans = set()
    while n:
        if sm >= n:
            ans.add(n)
            sm -= n
        n -= 1
    print('YES')
    print(len(ans))
    print(*list(ans))
    ans = set(range(1, m + 1)) - ans
    print(len(ans))
    print(*list(ans))