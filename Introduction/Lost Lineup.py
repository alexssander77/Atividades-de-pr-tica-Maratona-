n = int(input())
ent = list(map(int, input().split()))

lineup = [0] * n
lineup[0] = 1

for i in range(1, n):
    position = ent[i - 1] + 1
    lineup[position] = i + 1

print(' '.join(map(str, lineup)))