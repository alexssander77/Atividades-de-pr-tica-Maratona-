while 1:
    n=int(input())
    if n==0:
        break
    while n>9:
        n=sum(int(digito) for digito in str(n))
    print(n)