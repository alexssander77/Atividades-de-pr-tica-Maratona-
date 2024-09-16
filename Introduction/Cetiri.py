a, b, c = map(int, input().split())
numbers = sorted([a, b, c])
d1 = numbers[1] - numbers[0]
d2 = numbers[2] - numbers[1]

if d1 == d2:
    print(numbers[2] + d1)
elif d1 > d2:
    print(numbers[0] + d2)
else:
    print(numbers[1] + d1)
