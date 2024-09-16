T = int(input())

for _ in range(T):
    num_instrucoes = int(input())
    instrucoes = []
    posicao = 0

    for i in range(num_instrucoes):
        instrucao = input().strip()

        if instrucao == "LEFT":
            instrucoes.append(-1)
            posicao -= 1
        elif instrucao == "RIGHT":
            instrucoes.append(1)
            posicao += 1
        else:
            partes = instrucao.split()
            indice = int(partes[2]) - 1
            acao = instrucoes[indice]
            instrucoes.append(acao)
            posicao += acao

    print(posicao)
