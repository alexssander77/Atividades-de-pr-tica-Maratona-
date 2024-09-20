n = int(input())
resp = "Anywhere is fine I guess"

for i in range(n):
    p = int(input())
    pratos = []
    nome_restaurante = input()
    for j in range(p):
        pratos.append(input().strip())

    if "pea soup" in pratos and "pancakes" in pratos:
        resp = nome_restaurante
        break

print(resp)
