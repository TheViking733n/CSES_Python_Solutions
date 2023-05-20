# Recursive version: compressed
solve = lambda n,ans : ans if n == 1 else solve(n - 1, ['0' + x for x in ans] + ['1' + x for x in ans][::-1])
print(*solve(int(input()), ['0', '1']), sep='\n')



'''
# Recursive version
 
ans = ['0', '1']
def solve(n, ans):
    if n == 1:
        return ans
    else:
        left = ['0' + x for x in ans]
        right = ['1' + x for x in ans]
        return solve(n - 1, left + right[::-1])
    
 
n = int(input())
print(*solve(n, ans), sep='\n')

'''




'''
# Iterative version

def grayCode(i):
    return i ^ (i >> 1)

def binary(x, n):
    ans = bin(x)[2:]
    return '0' * (n - len(ans)) + ans

n = int(input())
for i in range(1 << n):
    print(binary(grayCode(i), n))
'''