import sys
input = sys.stdin.readline

n = int(input())
arr = []
ans = 0
for i in range(n):
    dur, en = map(int, input().split())
    ans += en
    arr.append(dur)
arr.sort()
sm = 0
for i in arr:
    sm += i
    ans -= sm
print(ans)