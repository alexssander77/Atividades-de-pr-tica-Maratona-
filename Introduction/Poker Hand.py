import collections

entrada = input().strip()
cartas = entrada.split()

ranks = [carta[0] for carta in cartas]
frequencias = collections.Counter(ranks)
max_frequencia = max(frequencias.values())

print(max_frequencia)
