while True:
    try:
        s1=input().strip()
        s2=input().strip()
        soma1=0
        soma2=0
        for char in s1.lower():
            if char.isalpha():
                soma1+= ord(char)-ord('a')+1

        for char in s2.lower():
            if char.isalpha():
                soma2+= ord(char)-ord('a')+1

        while soma1 > 9:
            soma1 = sum(int(digito) for digito in str(soma1))


        while soma2 > 9:
            soma2 = sum(int(digito) for digito in str(soma2))

        if soma1 > 0 and soma2 > 0:
            if soma1 > soma2:
                coef = soma2 / soma1
            else:
                coef = soma1 / soma2

            print(f"{coef * 100:.2f} %")
        else:
            print("0.00 %")


    except EOFError:
        break