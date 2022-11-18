# Enter your code here. Read input from STDIN. Print output to STDOUT
import math 
def nCr(n,r):

    f = math.factorial

    return f(n) // f(r) // f(n-r)
N = int(input())
distance = N - 1
n = math.ceil(distance/3)
m = distance%3
if distance == 0:
    ans = 0
    n = 0
else:
    if m == 1:
        ans = nCr(n+1, n-1)
    elif m == 2:
        ans = n
    elif m == 0:
        ans = 1
    
print(n, ans%1000000007)