from functools import reduce
import itertools
T = int(input())
for _ in range(T):
    Lines, Length = map(int, input().split())
    numbers = []
    for _ in range(Lines):
        numbers.append(int(input(), 2))
    counter = 0
    for comb in itertools.combinations(numbers, 3):
        res = reduce(lambda x, y: x | y, comb)
        if res == (1 << Length) - 1:
            counter += 1
    print(counter)