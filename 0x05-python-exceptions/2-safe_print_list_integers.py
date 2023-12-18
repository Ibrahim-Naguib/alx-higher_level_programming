#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i, j = 0, 0
    while i is not x:
        try:
            print("{:d}".format(my_list[i]), end="")
            j += 1
        except (TypeError, ValueError):
            pass
        i += 1
    print()
    return j
