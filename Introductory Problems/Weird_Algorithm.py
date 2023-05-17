n = int(input())
ans = [n]
while n != 1:
    if n % 2 == 0: n //= 2
    else: n = n * 3 + 1
    ans.append(n)
print(*ans)