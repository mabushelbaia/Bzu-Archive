import itertools
flatten_itter = itertools.chain.from_iterable
def factors(n):
    return set(flatten_itter((i, n//i) for i in range(1, int(n**0.5) + 1) if n % i == 0))
T = int(input())
for _ in range(T):
    n = int(input())
    print(*sorted(factors(n)), sep=' ')