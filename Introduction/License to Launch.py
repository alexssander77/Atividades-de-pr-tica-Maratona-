n=int(input())
entrada=input().split()
menor=1000000
v=0
for i in range(n):
    if menor>int(entrada[i]):
        menor=int(entrada[i])
        v=i
print(v)