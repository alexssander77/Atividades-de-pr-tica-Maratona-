wrong_attempts = [0] * 26
total_time = 0
problems_solved = 0
solved_problems = set()

while True:
    line = input().strip()
    if line == '-1':
        break

    time, problem, result = line.split()
    time = int(time)
    problem_index = ord(problem) - ord('A')

    if problem_index not in solved_problems:
        if result == 'right':
            problems_solved += 1
            total_time += time + wrong_attempts[problem_index] * 20
            solved_problems.add(problem_index)
        elif result == 'wrong':
            wrong_attempts[problem_index] += 1

print(problems_solved, total_time)
