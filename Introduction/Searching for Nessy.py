t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    sonars = (n // 3) * (m // 3)
    print(sonars)