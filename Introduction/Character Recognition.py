n = int(input())
linhas = [input() for _ in range(5)]
resultado = []

for i in range(n):
    parte1 = linhas[0][i * 4:i * 4 + 3]
    parte2 = linhas[1][i * 4:i * 4 + 3]
    parte3 = linhas[2][i * 4:i * 4 + 3]
    parte4 = linhas[3][i * 4:i * 4 + 3]
    parte5 = linhas[4][i * 4:i * 4 + 3]

    digito = [parte1, parte2, parte3, parte4, parte5]

    if digito == ['.*.', '.*.', '.*.', '.*.', '.*.']:
        resultado.append('1')
    elif digito == ['***', '..*', '***', '*..', '***']:
        resultado.append('2')
    elif digito == ['***', '..*', '***', '..*', '***']:
        resultado.append('3')

print("".join(resultado))
