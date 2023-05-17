"""
1 -> 0
2 -> 0 	    | 0
3 -> 8 	    | 1  = n * (n - 1) // 2
4 -> 24 	| 3
5 -> 48 	| 6
6 -> 80 	| 10
7 -> 120 	| 15
8 -> 168 	| 21
9 -> 224 	| 28
10 -> 288 	| 36

i * i * (i * i - 1) // 2 - 4 * i (i - 1)
"""


print(0, *[((i + 1) * (i + 1) * ((i + 1) * (i + 1) - 1)) // 2 - 4 * i * (i - 1) for i in range(1, int(input()))], sep='\n')

# n = int(input())
# ans = 0
# mv = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
# for n in range(1, 11):
#     ans = 0
#     for i in range(n):
#         for j in range(n):
#             for di, dj in mv:
#                 x, y = i + di, j + dj
#                 if 0 <= x < n and 0 <= y < n:
#                     ans += 1
#     print(n, '->', ans//2, '\t|', ans//16)
# # print((n**2 * (n**2 - 1)) // 2 - ans//2)
        
                
