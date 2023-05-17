'''
2x + y = a
x + 2y = b

x = a - (a + b) // 3
y = b - (a + b) // 3
'''
for _ in range(int(input())):
    a, b = sorted(list(map(int, input().split())))
    x = a - (a + b) // 3
    y = b - (a + b) // 3
    print("YES" if x >= 0 and y >= 0 and 2 * x + y == a else "NO")