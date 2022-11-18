import math
n = int(input())
nums = input().split(" ")
G, ans = 0, 0
for i in range(n):
    G = math.gcd(G, int(nums[i]))
for i in range(1, G + 1):
    if i*i > G:
        break
    if not G%i:
        if i*i == G:
            ans += 1
        else:
            ans += 2
print(ans)