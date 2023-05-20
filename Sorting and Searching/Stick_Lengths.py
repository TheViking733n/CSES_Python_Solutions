"""
ans must be one of a[i]
if a[k] is answer then:
    Define left = a[k] * k - sum(a[0 .. k-1])
    Define right = sum(a[k+1 .. n-1]) - a[k] * (n-k-1)
    Then left + right should be minimum
So,
    left = a[i] * i - ps[i]
    right = ps[n] - ps[i+1] - a[i] * (n - i - 1)
Therefore,
    left + right = ps[n] - 2 * ps[i] + (2 * i - n) * a[i]
"""
n = int(input())
a = list(map(int, input().split()))
a.sort()
ps = [0]
for i in a: ps.append(ps[-1] + i)
ans = 1 << 60
for i in range(n):
    ans = min(ans, ps[n] - 2 * ps[i] + (2 * i - n) * a[i])
print(ans)


# # Greedy will fail
# avg = sum(a) // n
# ans1 = ans2 = 0
# for i in a:
#     ans1 += abs(avg - i)
#     ans2 += abs(avg + 1 - i)
# print(min(ans1, ans2))