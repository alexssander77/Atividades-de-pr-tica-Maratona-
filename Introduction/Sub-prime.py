def main():
    while True:

        B, N = map(int, input().split())


        if B == 0 and N == 0:
            break


        reservas = list(map(int, input().split()))


        for _ in range(N):
            devedor, credor, valor = map(int, input().split())
            reservas[devedor - 1] -= valor
            reservas[credor - 1] += valor


        if all(r >= 0 for r in reservas):
            print("S")
        else:
            print("N")


if __name__ == "__main__":
    main()
