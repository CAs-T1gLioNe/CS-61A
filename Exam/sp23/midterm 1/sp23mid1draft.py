def repeating(t, n):
    if pow(10, t-1) > n:
        return False
    rest = n
    # 2 6161616161
    while rest:
        if rest % pow(10, t) != n % pow(10, t):
            return False
        rest = rest // pow(10, t)
    return True


print(repeating(2, 616616))
