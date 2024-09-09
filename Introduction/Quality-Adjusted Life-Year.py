n=int(input())
total=0
for i in range(n):
    a, b = map(float, input().split())
    total=total+a*b
print(f"{total:.3f}")