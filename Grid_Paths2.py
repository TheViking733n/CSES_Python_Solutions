'''
Encoding Scheme:
U := 0
R := 1
D := 2
L := 3

48 * 2 = 96 bits
96 / 4 = 24 chars in hex
'''

move = 'RRRRRRDLLLLLLDRRRRRRDLLLLLLDRRRRRRDDLULDLULDLULD'

m = {
    'R': 1,
    'L': 3,
    'U': 0,
    'D': 2,
}
mInverse = "URDL"

def encodeMove(s):
    res = 0
    for i in range(len(s)):
        res |= m[s[i]] << (i * 2)
    return res

def decodeMove(x):
    res = []
    while x:
        res += mInverse[x & 3]
        x >>= 2
    return ''.join(res)

print(decodeMove(encodeMove(move)) == move)

inp = open('Grid_Paths.txt', 'r')
ans = []
for line in inp:
    line = line.strip()
    x = encodeMove(line)
    ans.append(x)

ans2 = []
for i in range(0, len(ans), 2):
    v1, v2 = ans[i], ans[i + 1]
    v = v1 << 96 | v2
    ans2.append(v & ((1 << 64) - 1))
    v >>= 64
    ans2.append(v & ((1 << 64) - 1))
    v >>= 64
    ans2.append(v & ((1 << 64) - 1))


with open('Grid_Paths_data.txt', 'w') as out:
    for x in ans2:
        out.write(hex(x) + ',\n')
