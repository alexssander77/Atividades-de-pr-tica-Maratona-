t = int(input())
for p in range(t):
    cartas = input().split()
    y = 0

    for _ in range(3):
        carta = cartas[0]
        if carta[0] in 'AKQJT':
            x = 10
        else:
            x = int(carta[0])

        y += x

        mover = cartas[:(10 - x) + 1]
        cartas = cartas[(10 - x) + 1:] + mover

    print(f"Case {p + 1}: {cartas[y - 1]}")








