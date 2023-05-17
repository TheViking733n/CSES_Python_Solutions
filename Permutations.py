'''
3 1 2
3 1 4 2
5 3 1 4 2
'''
n = int(input())
if 1 < n <= 3:
    print("NO SOLUTION")
    exit()
od, ev = n - 1 + (n & 1), n - (n & 1)
print(*list(range(od, 0, -2)), *list(range(ev, 1, -2)))