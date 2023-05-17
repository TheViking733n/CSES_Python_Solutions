def towerOfHanoi(n, left, middle, right, ans):
    if n == 1:
        ans.append(f"{left} {right}")
        return
    towerOfHanoi(n - 1, left, right, middle, ans)
    ans.append(f"{left} {right}")
    towerOfHanoi(n - 1, middle, left, right, ans)


ans = []
towerOfHanoi(int(input()), 1, 2, 3, ans)
print(len(ans), *ans, sep="\n")