t = int(input())
for i in range(t):
    total = 0
    n = int(input())
    votos = []

    for j in range(n):
        a = int(input())
        votos.append(a)
        total += a

    mais = max(votos)
    cont = votos.count(mais)

    if cont > 1:
        print("no winner")
    else:
        vencedor = votos.index(mais) + 1  # Adiciona 1 para o número do candidato
        if mais > total / 2:
            print(f"majority winner {vencedor}")
        else:
            print(f"minority winner {vencedor}")
