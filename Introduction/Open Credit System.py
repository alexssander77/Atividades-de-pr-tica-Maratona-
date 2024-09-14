t = int(input())

for _ in range(t):
    n = int(input())
    notas = []

    for _ in range(n):
        notas.append(int(input()))

    max_diferenca = float('-inf')
    max_senior = notas[0]

    for i in range(1, n):

        max_diferenca = max(max_diferenca, max_senior - notas[i])
        max_senior = max(max_senior, notas[i])


    print(max_diferenca)
