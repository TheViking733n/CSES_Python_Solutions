'''
ps[i] = sigma a[i]
count no. of (ps[j] - ps[i]) % n == 0
            => ps[j] ≡ ps[i] (mod n)
'''
from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
ps = [0]
for i in a: ps.append((ps[-1] + i) % n)
ans = 0
seen = defaultdict(int)
for i in ps:
    ans += seen[str(i)]
    seen[str(i)] += 1
print(ans)
