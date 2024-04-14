import string


def split(s):
    """Return a list of words contained in s, which are sequences of characters
    separated by whitespace (spaces, tabs, etc.).

    >>> split("It's a lovely day, don't you think?")
    ["It's", 'a', 'lovely', 'day,', "don't", 'you', 'think?']
    """
    return s.split()


# tlist = [3, 4, 1, 4, 5]
# tstring = 'ab'
# print(tstring[1:]+"+"+tstring[0])
# print(min(tlist))
# print(tlist.index(4))


tlist = [1, 4, 2, 8, 5, 7]
trange = range(9)

print(
    tlist.index(1),
    trange[3]
)
