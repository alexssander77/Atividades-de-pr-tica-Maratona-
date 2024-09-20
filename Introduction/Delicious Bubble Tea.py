n = int(input())
precos_chas = list(map(int, input().split()))
m = int(input())
precos_toppings = list(map(int, input().split()))

combinacoes = []
for i in range(n):
    dados = list(map(int, input().split()))
    combinacoes.append(dados[1:])

dinheiro = int(input())

menor_preco = float('inf')

for i in range(n):
    preco_cha = precos_chas[i]
    for topping in combinacoes[i]:
        preco_total = preco_cha + precos_toppings[topping - 1]
        menor_preco = min(menor_preco, preco_total)

if menor_preco > dinheiro:
    print(0)
else:
    max_estudantes = dinheiro // menor_preco
    print(max_estudantes - 1)
