n = int(input())
nu = n
s = 0
numeros = input().split()
for i in range(n):
    if int(numeros[i]) == -1:
        nu -= 1
    else:
        s += int(numeros[i])
media=float(s/nu)
print(media)