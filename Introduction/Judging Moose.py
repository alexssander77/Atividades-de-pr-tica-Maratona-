import sys

a, b=map(int, input().split())
conf = 0
r = 0
if (a == b == 0):
    print("Not a moose")
    sys.exit(0)
if (a > b):
    r = 2 * a
    conf = 1
elif (b>a):
    r=2*b
    conf=1
else:
    r=a+b
    conf = 0

if (conf == 1):
    print(f"Odd {r}")
else:
    print(f"Even {r}")
