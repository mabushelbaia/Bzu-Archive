
import math 
def nCr(n,r):

    f = math.factorial

    return f(n) // f(r) // f(n-r)
N, k = map(int, input().split())
distance = N - 1
n = math.ceil(distance/k)
m = distance%k
if distance == 0:
    ans = 0
    n = 0
else:
    if m == 0: 
        ans = 1
    else:
        ans = nCr(n+k-(m+1), n-1)
print(n, ans%1000000007)
