while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break

    cartas_alice = list(map(int, input().split()))
    cartas_betty = list(map(int, input().split()))

    conjunto_alice = set(cartas_alice)
    conjunto_betty = set(cartas_betty)

    unicas_alice = conjunto_alice - conjunto_betty
    unicas_betty = conjunto_betty - conjunto_alice
    max_trocas = min(len(unicas_alice), len(unicas_betty))

    print(max_trocas)

