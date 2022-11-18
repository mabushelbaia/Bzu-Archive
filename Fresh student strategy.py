n = int(input())
nums = list(map(int, input().split()))
if n <= 3:
    print(0)
else:
    nums.sort()
    print(sum(nums[3:]*2))