# Enter your code here. Read input from STDIN. Print output to STDOUT
string  = input()
Q = int(input())
for _ in range(Q):
    L, R, C = input().split()
    L, R = int(L), int(R)
    print((R-L+1) - string[L-1:R].count(C))