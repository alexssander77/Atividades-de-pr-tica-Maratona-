ma,n=map(int, input().split())
a=0
r=0
for i in range(n):
    s,q=map(str, input().split())
    if s=="enter":
        if int(q)+a>ma:
            r+=1
        else:
            a+=int(q)
    else:
        a-=int(q)
print(r)