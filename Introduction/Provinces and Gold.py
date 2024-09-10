a, b, c = map(int, input().split())

p = 3 * a + 2 * b + c
vit = 0
if p >= 8:
    vit = 1

elif p >= 5:
    vit = 2

elif p >= 2:
    vit = 3

if vit == 1:
    print("Province or", end=" ")
elif vit == 2:
    print("Duchy or", end=" ")
elif vit == 3:
    print("Estate or", end=" ")

if p >= 6:
    print("Gold")
elif p >= 3:
    print("Silver")
else:
    print("Copper")