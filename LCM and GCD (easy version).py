from math import gcd
def expression(a, b):
    return a*b/(gcd(a, b)**2)
T = int(input())
for _ in range(T):
    n, a = list(map(int, input().split()))
    print((n//a)*a)