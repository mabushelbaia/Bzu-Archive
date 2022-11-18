string = input()
counter = 0
left, right = 0, len(string) - 1 

while left <= right:
    counter += 1
    middle = (left + right)//2
    if string[middle] == "0":
        left = middle + 1
    else:
        right = middle - 1
print(counter)
