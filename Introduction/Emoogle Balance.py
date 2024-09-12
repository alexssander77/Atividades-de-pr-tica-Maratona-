cont=0
while 1:
    cont+=1
    nz=0
    nn=0
    n=int(input())
    if n==0:
        break
    entrada=input().split()
    for i in range(n):
        if int(entrada[i])==0:
            nz+=1
        else:
            nn+=1

    print(f"Case {cont}: {nn-nz}")