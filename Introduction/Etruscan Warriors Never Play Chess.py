import math

n = int(input())
for _ in range(n):
    w = int(input())
    k = int(math.floor((-1 + math.sqrt(1 + 8 * w)) / 2))
    print(k)
