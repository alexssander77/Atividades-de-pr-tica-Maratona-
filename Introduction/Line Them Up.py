n=int(input())

nomes=[input().strip() for _ in range(n)]
if nomes == sorted(nomes):
    print("INCREASING")
elif nomes==sorted(nomes, reverse=True):
    print("DECREASING")
else:
    print("NEITHER")
