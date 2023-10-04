from sys import argv

list_arg = argv[1:]
list_len = len(list_arg)
list_end = list_len - 1


def _print(frm, to):
    print(f"from {frm} to {to}")


pos = 0
while pos < list_len // 2:
    # cache
    l_c = list_arg[pos]
    r_c = list_arg[list_end - pos]
    # swap
    list_arg[pos] = r_c
    list_arg[list_end - pos] = l_c
    # forward
    pos += 1

_print("".join(argv[1:]), "".join(list_arg))
