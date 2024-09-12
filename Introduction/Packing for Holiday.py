t=int(input())
cont=0
for i in range(t):
    cont+=1
    a, b, c=map(int, input().split())
    if a<=20 and b<=20 and c<=20:
        print(f"Case {cont}: good")
    else:
        print(f"Case {cont}: bad")