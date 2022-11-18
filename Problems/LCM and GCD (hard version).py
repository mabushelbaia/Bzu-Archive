from math import gcd
for _ in range(int(input())):
    n, a = list(map(int, input().split()))
    for b in range(n, a, -1):
        if gcd(a, b) == 1:
            print(b)
            break