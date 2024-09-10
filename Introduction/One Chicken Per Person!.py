a,b=map(int, input().split())
resp=b-a
if resp>=0:
    if resp==1:
        print(f"Dr. Chaz will have {resp} piece of chicken left over!")
    else:
        print(f"Dr. Chaz will have {resp} pieces of chicken left over!")
else:
    if resp==-1:
        print(f"Dr. Chaz needs {abs(resp)} more piece of chicken!")
    else:
        print(f"Dr. Chaz needs {abs(resp)} more pieces of chicken!")hicken!")