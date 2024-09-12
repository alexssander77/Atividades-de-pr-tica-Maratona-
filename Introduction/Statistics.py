cont=0
while True:
    try:
        menor=1000000
        maior=-1000000
        cont+=1
        if cont>10:
            break
        entrada=input().split()
        for i in range(1, int(entrada[0])+1):
            if maior<int(entrada[i]):
                maior=int(entrada[i])
            if menor>int(entrada[i]):
                menor=int(entrada[i])
        print(f"Case {cont}: {menor} {maior} {maior-menor}")
    except EOFError:
        break