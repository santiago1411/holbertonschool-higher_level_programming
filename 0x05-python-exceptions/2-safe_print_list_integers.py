#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    errors = 0
    while count < x:
        try:
            print("{:d}".format(my_list[count]), end='')
            errors += 1
        except (ValueError, TypeError):
            pass
        finally:
            count += 1
    print()
    return count
