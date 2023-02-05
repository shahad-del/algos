tests = int(input())
results = []
for i in range(tests):
    problems,Break_time,solving_time = list(map(int,input().split()))
    overall_time = []
    for i in range(problems):
        if problems == 1:
            total_time = (problems*solving_time)
            overall_time.append(total_time)
            break
        elif problems % 2 != 0:
            solved_problems = (problems + 1)//2
            total_time = (solved_problems*solving_time)+Break_time
            problems = problems- solved_problems
            solving_time = solving_time*2
            overall_time.append(total_time)
        else:
            solved_problems = problems//2
            total_time = (solved_problems*solving_time)+Break_time
            problems = problems- solved_problems
            solving_time = solving_time*2
            overall_time.append(total_time)
    results.append(sum(overall_time))
    overall_time = []
for time in results:
    print(time)
