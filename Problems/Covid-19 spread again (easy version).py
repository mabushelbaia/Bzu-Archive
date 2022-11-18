# K is odd
# odd * odd = odd
# even * odd = even
# number doesn't change

# K is even
# even * even = even
# odd * even = even
# number 

T = int(input())
for t in range(T):
    n, d, k = map(int, input().split())
    array = list(map(int, input().split()))
    if k%2 == 1: # odd
        print(len([elem for elem in array if elem%2 == 1]))
    else: # even
        print(0)