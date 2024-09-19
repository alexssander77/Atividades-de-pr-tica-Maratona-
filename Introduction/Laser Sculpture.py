while True:
    A, C = map(int, input().split())
    if A == 0 and C == 0:
        break

    alturas = list(map(int, input().split()))
    ligacoes = 0
    altura_atual = A
    for i in alturas:
        if i < altura_atual:
            ligacoes += altura_atual - i
        altura_atual = i
    print(ligacoes)
