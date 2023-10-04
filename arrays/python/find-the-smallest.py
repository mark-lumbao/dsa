# Recursive Function
# that returns the smallest numeric argument
# Reference:
# https://www.geeksforgeeks.org/introduction-to-recursion-data-structure-and-algorithm-tutorials/

from sys import argv


_int_list = [0] * len(argv[1:])
count = 0

for i in argv[1:]:
    _int_list[count] = int(i)
    count += 1


def get_smallest(list: list[int]):
    first: int = list[0]
    remaining = list[1:]

    if len(list) <= 1:
        return first
    else:
        remaining_smallest: int = get_smallest(remaining)
        return first if first < remaining_smallest else remaining_smallest


print(get_smallest(_int_list))
