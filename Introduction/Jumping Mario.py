t=int(input())
cont=0
for i in range(t):
    cont+=1
    n=int(input())
    pa=0
    pb=0
    entrada=input().split()
    if n==1:
        print(f"Case {cont}: 0 0")
    else:
        for j in range(1,n):
            if int(entrada[j])<int(entrada[j-1]):
                pb+=1
            elif int(entrada[j])>int(entrada[j-1]):
                pa+=1

        print(f"Case {cont}: {pa} {pb}")