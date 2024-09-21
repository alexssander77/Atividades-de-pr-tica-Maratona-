a,b=map(int, input().split())
lista = list(map(int, input().split()))
if b==1:
    print(7)
elif b==2:
    if lista[0]>lista[1]:
        print("Bigger")
    elif lista[0]==lista[1]:
        print("Equal")
    else:
        print("Smaller")
elif b ==3:
    mediana=[lista[0],lista[1],lista[2]]
    mediana.sort()
    print(mediana[1])

elif b ==4:
    soma=sum(lista)
    print(soma)
elif b ==5:
    som=0
    for num in lista:
        if num%2==0:
            som+=+num
    print(som)

elif b ==6:
    porc=[]
    for i in range(a):
        porc.append(lista[i]%26)
    for i in range(a):
        print(chr(porc[i]+97), end='')
elif b == 7:
    index = 1
    Vindices = []

    while True:
        if index < 0 or index >= a:
            print("Out")
            break
        if index in Vindices:
            print("Cyclic")
            break
        if index == a - 1:
            print("Done")
            break

        Vindices.append(index)
        index = lista[index]