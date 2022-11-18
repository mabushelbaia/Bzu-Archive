def getdivisible(L, R, N): #1 10 3
    left, right = 0, 0
    if L%N == 0:
        left = L
    else:
        left = ((L+N)//N)*N
    if R%N == 0:
        right = R
    else:
        right = ((R)//N)*N
    return int((right - left)//N + 1)
from math import gcd
L, R, N, M = map(int, input().split())
print(getdivisible(L, R, N)+getdivisible(L, R, M)-getdivisible(L, R, N*M/gcd(N, M)))



