from itertools import permutations
s = input()
ans = sorted(set(permutations(s, len(s))))
print(len(ans), *[''.join(i) for i in ans], sep='\n')