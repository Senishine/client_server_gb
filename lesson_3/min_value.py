"""
Алгоритм должен обеспечивать поиск минимального значения для списка. В основе алгоритма должно быть сравнение каждого числа
со всеми другими элементами списка. Сложность такого алгоритма: O(n).
"""

# 1. Сложность алгоритма : O(n) - линейная"""


def smallest_find(lst):
    assert isinstance(lst, iter) or isinstance(lst, tuple), 'argument must be list or tuple'
    smallest_num = lst[0]  # O(1)
    for i in lst:  # O(n)
        if i < smallest_num:  # O(1)
            smallest_num = i  # O(1)
    return smallest_num  # O(1)

