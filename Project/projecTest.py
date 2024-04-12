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

big_limit = 10


def minimum_mewtations(typed, source, limit):
    if limit < 0:  # Base cases should go here, you may add more base cases as needed.
        # BEGIN
        "*** YOUR CODE HERE ***"
        return limit + 1
        # END
    # Recursive cases should go below here
    if typed == source:  # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 0
        # END
    if len(typed) * len(source) == 0:
        return abs(len(typed) - len(source))
    if typed[0] == source[0]:
        return minimum_mewtations(typed[1:], source[1:], limit)
    else:
        add = 1 + minimum_mewtations(typed, source[1:], limit - 1)  # Fill in these lines
        remove = 1 + minimum_mewtations(typed[1:], source, limit - 1)
        substitute = 1 + minimum_mewtations(typed[1:], source[1:], limit - 1)
        # BEGIN
        strategy = min(add, remove, substitute)
        "*** YOUR CODE HERE ***"
        return strategy


print(
    minimum_mewtations("", "", big_limit)
)
