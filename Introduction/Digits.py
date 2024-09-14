import sys


for line in sys.stdin:
    line = line.strip()

    if line == "END":
        break


    k = 1


    current = line

    while True:

        next_val = str(len(current))


        if current == next_val:
            print(k)
            break


        current = next_val
        k += 1