grid = [input() for i in range(8)]
notAllowed = set()
for i in range(8):
    for j in range(8):
        if grid[i][j] == '*': notAllowed.add((i, j))

def isAttacking(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

def solve(x1, moves, ans, notAllowed):
    if x1 == 8:
        ans[0] += 1
        return
    for y1 in range(8):
        if (x1, y1) in notAllowed:
            continue
        f = 0
        for x, y in moves:
            if isAttacking(x1, y1, x, y):
                f = 1
                break
        if f: continue
        moves.append((x1, y1))
        solve(x1 + 1, moves, ans, notAllowed)
        moves.pop()

ans = [0]
solve(0, [], ans, notAllowed)
print(*ans)
        
            