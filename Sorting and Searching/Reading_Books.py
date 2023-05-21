n = int(input())
arr = [int(i) for i in input().split()]
mx, total = max(arr), sum(arr)
sm = total - mx
print(total if mx <= sm else 2 * mx)

