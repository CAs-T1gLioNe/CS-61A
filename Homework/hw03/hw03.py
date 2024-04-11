LAB_SOURCE_FILE=__file__


HW_SOURCE_FILE=__file__


def num_eights(n):
    """Returns the number of times 8 appears as a digit of n.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 0
    else:
        return (n % 10 == 8) + num_eights(n // 10)


def digit_distance(n):
    """Determines the digit distance of n.

    >>> digit_distance(3)
    0
    >>> digit_distance(777)
    0
    >>> digit_distance(314)
    5
    >>> digit_distance(31415926535)
    32
    >>> digit_distance(3464660003)
    16
    >>> from construct_check import check
    >>> # ban all loops
    >>> check(HW_SOURCE_FILE, 'digit_distance',
    ...       ['For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if abs(n) < 10:
        return 0
    elif abs(n) < 100:
        return abs((n % 10) - (n // 10))
    else:
        return abs((n % 10) - (n // 10 % 10)) + digit_distance(n // 10)


def interleaved_sum(n, odd_func, even_func):
    """Compute the sum odd_func(1) + even_func(2) + odd_func(3) + ..., up
    to n.

    >>> identity = lambda x: x
    >>> square = lambda x: x * x
    >>> triple = lambda x: x * 3
    >>> interleaved_sum(5, identity, square) # 1   + 2*2 + 3   + 4*4 + 5
    29
    >>> interleaved_sum(5, square, identity) # 1*1 + 2   + 3*3 + 4   + 5*5
    41
    >>> interleaved_sum(4, triple, square)   # 1*3 + 2*2 + 3*3 + 4*4
    32
    >>> interleaved_sum(4, square, triple)   # 1*1 + 2*3 + 3*3 + 4*3
    28
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'interleaved_sum', ['While', 'For', 'Mod']) # ban loops and %
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return odd_func(1)
    return odd_func(n) * (n & 1) + even_func(n) * (1 - n & 1) + interleaved_sum(n - 1, odd_func, even_func)



def next_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> next_larger_coin(1)
    5
    >>> next_larger_coin(5)
    10
    >>> next_larger_coin(10)
    25
    >>> next_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def next_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> next_smaller_coin(25)
    10
    >>> next_smaller_coin(10)
    5
    >>> next_smaller_coin(5)
    1
    >>> next_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1

def count_coins(total):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def startwithc(coin, remained):
        if not coin:
            return 0
        remaining = remained - coin
        next_coin = next_smaller_coin(coin)
        if remained == 0:
            return 1
        elif remained < 0:
            return 0
        else:
            return startwithc(coin, remaining) + startwithc(next_coin, remained)

    return startwithc(25, total)


# some extra practice on Recursion

'''
Problem 1: Digital(from Fall 2017 MT1 Q4a)

Implement collapse, which takes a non-negative integer, and returns the result of removing all digits 
from it that duplicate the digit immediately to their right. 
    def collapse(n):
        """
        For non-negative N, the result of removing all digits that are equal to the digit on their right,
        so that no adjacent digits are the same. 
        >>> collapse(1234) 1234 
        >>> collapse(12234441) 12341 
        >>> collapse(0) 0 
        >>> collapse(3) 3 
        >>> collapse(11200000013333) 12013
        """
        left, last = n // 10, n % 10
        if ___: 
            return last
        elif ___ == ___:
            return collapse(___)
        else:
            return collapse(___) * 10 + ___
'''


def collapse(n):
    left, last = n // 10, n % 10
    if n < 10:
        return last
    elif left % 10 == last:
        return collapse(left)
    else:
        return collapse(left)*10 + last


'''
Problem 2: Won’t You Be My Neighbor?(from Summer 2018 MT1 Q5a)

Write repeat_digits, which takes a positive integer n and returns another integer that is identical to n
but with each digit repeated. 
def repeat_digits(n):
    """Given a positive integer N, returns a number with each digit repeated.
    >>> repeat_digits(1234) 11223344
    """
    last, rest = ___, ___
    if ___:
        return ___
    return ___(___) * ___ + ___
'''
# 该题与上一题几乎一样，唯一的区别是主干中少了一条用来说明 base case 的 if 语句，需要在别的地方补上
# 但是在第一次编写方法的时候由于在最后 return 语句中少了一个括号导致结果离谱，不过计算机不会说谎，一定是我错了，最终发现了问题


def repeat_digits(n):
    last, rest = n % 10, n // 10
    print(last, rest)
    if last == rest % 10:
        return repeat_digits(rest) if rest > 10 else rest
    return (repeat_digits(rest) * 10 if rest > 10 else rest * 10) + last
# 起初 last 前没有括号导致 else 认为 rest*10 + last 是一个整体


'''
Problem 3: Palindromes(from Fall 2019 Final Q6b)

Implement contains, which takes non-negative integers a and b.
It returns whether all of the digits of a also appear in order among the digits of b.
Important: You may not write str, repr, list, tuple, [, or ].
def contains(a, b):
    """
    Return whether the digits of a are contained in the digits of b.
    >>> contains(357, 12345678) True
    >>> contains(753, 12345678) False
    >>> contains(357, 37) False 
    """
    if a == b:
        return True
    if ___ > ___:
        return False
    if ___ == ___:
        return contains(___, ___)
    else:
        return contains(___, ___)
'''
# 一遍过，轻松愉快


def contains(a, b):
    if a == b:
        return True
    if a > b:
        return False
    if a % 10 == b % 10:
        return contains(a // 10, b // 10)
    else:
        return contains(a, b // 10)


'''
下题为汉诺塔问题的基本问题，三根柱子，第一根柱子上叠有n个圆盘，上小下大，目标是将这n个盘移到第三根柱子上，过程中每根柱子都需遵循上小下大
将圆盘编号，最小为1递增。考虑将n个圆盘从某柱移到另一柱，则等效于将盘1~n-1移指空闲柱，然后将盘n移到目标柱，再将盘1~n-1移到目标盘，类似等效
ez一遍过
'''


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    rod = [1, 2, 3]
    rod.remove(start)
    rod.remove(end)
    empty_rod = rod[0]
    if n == 1:
        print_move(start, end)
    else:
        move_stack(n-1, start, empty_rod)
        move_stack(1, start, end)
        move_stack(n-1, empty_rod, end)


from operator import sub, mul


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial',
    ...     ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'
