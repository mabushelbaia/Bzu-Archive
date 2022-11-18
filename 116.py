Lenghth = input()
string = input()
one_counter = 0 
answer = 0
for num in string:
    if num == '1':
        one_counter += 1
    else:
        if one_counter >= 2:
            one_counter -= 2
            answer += 1
        else:
            one_counter = 0
print(answer)