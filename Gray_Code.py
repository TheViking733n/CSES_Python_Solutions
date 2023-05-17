def grayCode(i):
    return i ^ (i >> 1)

def binary(x, n):
    ans = bin(x)[2:]
    return '0' * (n - len(ans)) + ans

n = int(input())
for i in range(1 << n):
    print(binary(grayCode(i), n))