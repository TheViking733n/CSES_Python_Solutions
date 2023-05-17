from collections import Counter
c = Counter(input())
ev, od = [], []
for k in c:
    if c[k] & 1: od.append(k * c[k])
    else: ev.append(k * (c[k] // 2))
if len(od) > 1: print("NO SOLUTION")
else: print("".join(ev) + "".join(od) + "".join(ev[::-1]))
