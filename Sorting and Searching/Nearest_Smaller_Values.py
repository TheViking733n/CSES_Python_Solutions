
# =========================================================================
# Approach similar to NGE problem

'''
cur   | stack
2       [5]
3       [2]
8       [2, 3]
4       [2, 3, 8]
1       [1]
5       [1, 5]
2       [1, 2]
'''

n = int(input())
arr = [int(i) for i in input().split()]

stack = [n-1]
ans = [-1] * n

for i in range(n-2, -1, -1):
    cur = arr[i]
    while stack and cur < arr[stack[-1]]:
        ans[stack.pop()] = i
    stack.append(i)
    # print(cur, [arr[i] for i in stack])
print(*[i+1 for i in ans])

