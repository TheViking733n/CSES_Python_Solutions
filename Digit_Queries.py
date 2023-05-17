"""
1 1 1 .. 1   2 2 2 .. 2   3 3 3 .. 3
      ^            ^            ^
  9 times     90 times    900 times

1 * 9
2 * 90
3 * 900
...
...
18 * 9e17

"""
for _ in range(int(input())):
    left = k = int(input())
    sm = 0
    numDigits = 1
    for i in range(18):
        cur = (i + 1) * 9 * 10 ** i
        sm += cur
        if k > sm:
            numDigits += 1
            left = k - sm
        else:
            break

    quot, rem = (left - 1) // numDigits, (left - 1) % numDigits
    ans = 10 ** (numDigits - 1) + quot
    print(str(ans)[rem])