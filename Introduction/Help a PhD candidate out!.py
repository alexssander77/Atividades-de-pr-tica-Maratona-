n = int(input())
for i in range(n):
    entrada = input()

    if entrada == "P=NP":
        print("skipped")
    else:
        a, b = map(int, entrada.split('+'))
        print(a + b)