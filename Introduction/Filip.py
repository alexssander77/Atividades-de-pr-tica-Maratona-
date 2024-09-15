n,n1=map(int, input().split())
a=(n%10*100)+(n//10%10*10)+(n//100)
b=(n1%10*100)+(n1//10%10*10)+(n1//100)
if a>b:
    print(a)
else:
    print(b)