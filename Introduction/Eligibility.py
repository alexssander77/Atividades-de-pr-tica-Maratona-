
n = int(input())

for _ in range(n):
    student = input()

    parts = student.split()
    name = parts[0]
    start_date = parts[1]
    birth_date = parts[2]
    courses = int(parts[3])

    start_year = int(start_date.split('/')[0])
    birth_year = int(birth_date.split('/')[0])

    if start_year >= 2010:
        print(f"{name} eligible")
    elif birth_year >= 1991:
        print(f"{name} eligible")
    elif courses >= 41:
        print(f"{name} ineligible")
    else:
        print(f"{name} coach petitions")
