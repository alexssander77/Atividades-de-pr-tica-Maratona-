while(1):
    a,b,c,d=map(int, input().split())
    if 0==a==b==c==d:
        break

    else:
        if a>b:
            soma1=a*10+b
        elif b>a:
            soma1=b*10+a
        else:
            soma1=1000+a
        if c>d:
            soma2=c*10+d
        elif d>c:
            soma2=d*10+c
        else:
            soma2=1000+c

        if soma2==21 and soma1!=21:
            print("Player 2 wins.")
        elif soma1==21 and soma2!=21:
            print("Player 1 wins.")
        elif soma2>soma1:
            print("Player 2 wins.")
        elif soma1>soma2:
            print("Player 1 wins.")
        else:
            print("Tie.")