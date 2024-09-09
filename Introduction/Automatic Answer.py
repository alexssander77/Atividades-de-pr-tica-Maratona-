n=int(input())
for i in range(n):
    num=int(input())
    total=(((num*567/9)+7492)*235/47)-498
    total=abs(total)
    resp=int(total//10%10)
    print(resp)