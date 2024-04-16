# a = [i*i if i % 2 == 0 else i-10 for i in [1, 2, 3, 4]]
# print(4 in a)
#
# b = [1, 2, 1 + 2]
# print(b, b*2)
#
# r = range(3, 6)
# print([r[0], r[2]])
# print(list(range(10)))
# print(b+[1])
#
# length = len(b)

fprices = {'oranges': 4, 'apples': 3, 'bananas': 2, 'kiwis': 9}
required_fruits = ['apples', 'oranges', 'bananas']
print(*[['1 ' + fruit] for fruit in required_fruits])

def buy(required_fruits, prices, total_amount):
    """
    Print ways to buy some of each fruit so that the sum of prices is amount.
    >>> prices = {'oranges': 4, 'apples': 3, 'bananas': 2, 'kiwis': 9}
    >>> buy(['apples', 'oranges', 'bananas'], prices, 12)
    [2 apples][1 orange][1 banana]
    >>> buy(['apples', 'oranges', 'bananas'], prices, 16)
    [2 apples][1 orange][3 bananas]
    [2 apples][2 oranges][1 banana]
    >>> buy(['apples', 'kiwis'], prices, 36)
    [3 apples][3 kiwis]
    [6 apples][2 kiwis]
    [9 apples][1 kiwi]
    """
    left = total_amount - sum([prices[fruit] for fruit in required_fruits])
    if left < 0:
        print('not enough money')
    if left == 0:
        print(*[['1 ' + fruit for fruit in required_fruits]])


tlist = [[1, 2], [2, 3]]
print(*tlist)
