cont=0

t=int(input())
for i in range(t):
    maior = -1000000
    cont += 1
    entrada=input().split()
    for i in range(1, int(entrada[0])+1):
        if maior<int(entrada[i]):
            maior=int(entrada[i])

    print(f"Case {cont}: {maior}")
