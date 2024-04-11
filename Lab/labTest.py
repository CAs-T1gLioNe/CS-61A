a = [i*i if i % 2 == 0 else i-10 for i in [1, 2, 3, 4]]
print(4 in a)

b = [1, 2, 1 + 2]
print(b, b*2)

r = range(3, 6)
print([r[0], r[2]])
print(list(range(10)))
print(b+[1])

length = len(b)


def sums(n, m):
    """Return lists that sum to n containing positive numbers up to m that
    have no adjacent repeats.

    >>> sums(5, 1)
    []
    >>> sums(5, 2)
    [[2, 1, 2]]
    >>> sums(5, 3)
    [[1, 3, 1], [2, 1, 2], [2, 3], [3, 2]]
    >>> sums(5, 5)
    [[1, 3, 1], [1, 4], [2, 1, 2], [2, 3], [3, 2], [4, 1], [5]]
    >>> sums(6, 3)
    [[1, 2, 1, 2], [1, 2, 3], [1, 3, 2], [2, 1, 2, 1], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    if n < 0:
        return []
    if n == 0:
        sums_to_zero = []       # The only way to sum to zero using positives
        return [sums_to_zero]   # Return a list of all the ways to sum to zero
    result = []
    for k in range(1, m + 1):
        result = result + [[k] + rest for rest in sums(n-k, m) if rest == [] or k != rest[0]]
    return result


print(a, length)
print(a)
