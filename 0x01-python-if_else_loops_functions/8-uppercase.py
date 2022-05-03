#!/usr/bin/python3
def uppercase(str):
    for i in str:
        pt = ord(i)
        if pt >= 97 and pt <= 122:
            pt -= 32
    print(f"{chr(pt)}", end='')
    print()
