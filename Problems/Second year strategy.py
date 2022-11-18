
N = int(input())
array = []
for _ in range(N):
    hours, grades = map(int, input().split())
    array.append((hours, grades))
ans = [0, 0, 0]
max_score, temp = 0, 0
for i in range(1 << N):
    pass_fail, score, pass_fail_hours = 0, 0, 0
    for j in range(N):
        if(1 << j) & i:
            score += array[j][0] * array[j][1]
        else:
            pass_fail_hours += array[j][0]
            pass_fail += 1
    if pass_fail_hours > 6:
        continue
    if pass_fail_hours > temp:
        temp = pass_fail_hours
        max_score = score
        ans[0] = pass_fail_hours
        ans[1] = score
        ans[2] = pass_fail
        continue
    elif pass_fail_hours == temp:
        if score > max_score:
            max_score = score
            ans[0] = pass_fail_hours
            ans[1] = score
            ans[2] = pass_fail
        elif score == max_score:
            if pass_fail < ans[2]:
                ans[0] = pass_fail_hours
                ans[1] = score
                ans[2] = pass_fail
print(*ans)