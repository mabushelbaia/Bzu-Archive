import math
T = int(input())
for _ in range(T):
    n = input()
    string = input()
    o_count = 0
    current_max = 0
    start_flag = False
    if string.count("S") == 0:
        print(-1)
    else:
        for i, ch in enumerate(string):
            if ch == "S" and start_flag:
                current_max = max(current_max, math.ceil(o_count/2))
                o_count = 0
            elif (ch == "S") and not start_flag:
                start_flag = True
                current_max = max(o_count, current_max)
                o_count = 0
            else:
                if i == len(string) - 1:
                    current_max = max(current_max, o_count+1)
                o_count += 1
        print(current_max)