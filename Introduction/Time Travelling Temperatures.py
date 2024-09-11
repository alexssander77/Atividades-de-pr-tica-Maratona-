import sys
a, b=map(float, input().split())
if b==1 and a==0:
    print("ALL GOOD")
    sys.exit(0)
elif b==1 and a!=0:
    print("IMPOSSIBLE")
    sys.exit(0)

result=a/(1-b)

if result.is_integer():
    print(f"{int(result)}")
else:
    print(f"{result:.6f}")