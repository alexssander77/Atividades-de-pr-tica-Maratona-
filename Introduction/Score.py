t=int(input())
for j in range(t):
    total=0
    s=str(input())
    mais=1
    for char in s:
        if char=='O':
            total+=mais
            mais+=1
        else:
            mais=1

    print(total)
