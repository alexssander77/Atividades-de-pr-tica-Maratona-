t=int(input())
for num in range(t):
    v=0
    entrada=input().split()

    for i in range(2,int(entrada[0])+1):
        if int(entrada[i])-1!=int(entrada[i-1]):
            v=i-1
    print(v)