import sys
s=str(input().strip())
b=0
for char in s:
    if b==1 and char=='s':
        print("hiss")
        sys.exit(0)
    elif char=='s':
        b=1
    else:
        b=0
print("no hiss")