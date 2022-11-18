T = int(input())
for _ in range(T):
    length = input()
    s = input()
    print(s.count("A")*s.count("G")*s.count("C")*s.count("T"))