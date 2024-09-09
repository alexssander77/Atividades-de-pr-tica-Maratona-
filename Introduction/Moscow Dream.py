a,b,c,n=map(int, input().split())
conf=0
if(a+b+c<n):
    conf=1

if(a<1 or b<1 or c<1 or n<3):
    conf=1

if(conf==1):
    print("NO")
else:
    print("YES")