while True:
    try:
        entrada = input().split()
        v = int(entrada[0])
        t = int(entrada[1])
        to=v*t*2
        print(to)
    except EOFError:
        break