while True:
    try:
        N, B, H, W = map(int, input().split())
        menor_custo = B + 1

        for _ in range(H):
            preco_pessoa = int(input())
            camas_disponiveis = list(map(int, input().split()))
            for camas in camas_disponiveis:
                if camas >= N:
                    custo_total = preco_pessoa * N
                    if custo_total <= B:
                        menor_custo = min(menor_custo, custo_total)

        
        if menor_custo <= B:
            print(menor_custo)
        else:
            print("stay home")

    except EOFError:
        break
