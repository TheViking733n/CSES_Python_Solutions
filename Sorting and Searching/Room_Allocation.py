def encode3(st, en, idx): return st << 52 | en << 20 | idx
def decode3(x): return x >> 52, x >> 20 & 0xffffffff, x & 0xfffff
def encode(st, en): return st << 20 | en
def decode(x): return x >> 20, x & 0xfffff

import sys
from heapq import heappop, heappush, heapify
input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arrival = [encode(arr[i][0], i) for i in range(n)]
arrival.sort()
ans = [-1] * n
pq = []
availableRooms = list(range(1, n+1))
heapify(availableRooms)

for x in arrival:
    st, idx = decode(x); en = arr[idx][1]  # out time of this customer

    # Remove all the customers who left before comming of this new customer
    while pq:
        en1, emptyRoom = decode(pq[0])
        if en1 < st:   # Remove this customer
            heappop(pq)
            heappush(availableRooms, emptyRoom)
        else:
            break
    
    # Allot one room to new customer
    room = heappop(availableRooms)
    heappush(pq, encode(en, room))
    ans[idx] = room

print(max(ans))
print(*ans)

    

