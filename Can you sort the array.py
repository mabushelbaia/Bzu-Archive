n = int(input())
nums = input().split(" ")
temp = n
for i in range(n - 1, -1 , -1):
    if (int(nums[i]) == temp): temp -= 1

print(temp)