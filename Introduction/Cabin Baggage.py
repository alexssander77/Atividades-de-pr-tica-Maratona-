t=int(input())
n=0
for i in range(t):
    a,b,c,d=map(float, input().split())
    if  (a+b+c>125 and (a>56 or b>45 or c>25)) or d>7:
        print("0")
    else:
        print("1")
        n+=1
print(n)