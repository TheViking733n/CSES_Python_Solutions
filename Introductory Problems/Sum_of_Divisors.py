# https://mathoverflow.net/questions/195325/how-to-calculate-the-sum-of-remainders-of-n


n = int(input())
sqrt = int(n **.5)

ans = 0
for i in range(1, sqrt + 1):
    ans += (n // i - sqrt) * i + (n // i) * (n // i + 1) // 2
    ans %= 1000000007
print(ans)









# n = int(input())
# sqrt = int(n **.5)
# ans = 0
# for i in range(1, sqrt + 1):  # O(sqrt(N))
#     ans += n // i
# ans = ans * 2 - sqrt * sqrt
# print(ans)

# n = 5

# sqrt = int(n **.5)
# sum1 = sum2 = 0
# for i in range(1, n + 1):   # O(N)
#     sum1 += i*(n // i)
# for i in range(1, sqrt + 1):  # O(sqrt(N))
#     sum2 += n // i
# sum2 = sum2 * 2 - sqrt * sqrt   
# print(sum1, sum2)

# n = 61
# sm = 0
# for i in range(1, n + 1):
#     # print(i, n % i, sep=' -> ')
#     sm += n % i
# print(sm)


# '''

# 0, 1, .. 49 | l = n//2 - 1
# 0, 2, .. 32 | l = n//3 - 1
# 1, 4, .. 22 | l = 
# 0, 4, .. 16 | l = 
# 0, 5, .. 15
# 4,    .. 10


# 0 -> 1 -> 35 -> 35
# 1 -> 2 -> 23 -> 23
# 2 -> 3 -> 17 -> 17
# 3 -> 4 -> 11 -> 14
# 1 -> 5 -> 11 -> 11
# 5 -> 6 -> 5 -> 10
# 1 -> 7 -> 8 -> 8
# 7 -> 8 -> 7 -> 7
# '''

# sqrt = int(n **.5)
# ans = 0
# for i in range(1, sqrt+1):  # O(sqrt(N))
#     first_term = n % i
#     common_diff = i
#     upper_limit = (n - 1) // (i + 1)
#     last_term = ((upper_limit - first_term) // common_diff) * common_diff + first_term
#     number_of_terms = (last_term - first_term) // common_diff + 1
#     ans += first_term + (first_term + last_term) * number_of_terms // 2
#     # print(first_term, common_diff, last_term, upper_limit, sep=' -> ')
#     if i == sqrt and first_term == last_term:
#         ans -= first_term
# print(ans)
