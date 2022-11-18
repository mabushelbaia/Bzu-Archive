def find_ans(N):
    while (N > 0):
        if (N % 5 == 3 or N % 5 == 4 or N%5 == 2):
            print("NO")
            return
        N //= 5
    print("YES")
T = int(input())
for _ in range(T):
    find_ans(int(input()))
