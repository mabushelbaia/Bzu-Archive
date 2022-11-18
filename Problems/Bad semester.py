# N avareage last semester
# M number of hour in this semester
# G the grade until now
# Y the number of remain exams
T = int(input())
for _ in range(T):
    raw_input = input()
    raw_input = raw_input.split(" ")
    N = int(raw_input[0])
    M = int(raw_input[1])
    G = int(raw_input[2])
    Y = int(raw_input[3])
    current_average = G / M
    minimum_average = N
    if current_average > minimum_average:
        print(0)
    else:
        if Y:
            grades = minimum_average*M - G
            print(grades)
        else:
            print(-1)
