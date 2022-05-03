#!/usr/bin/python3
for i in reversed(range(97, 123)):
    if (i % 2 == 0):
        print(f"{chr(i)}", end='')
    else:
        print(f"{chr(i - 32)}", end='')
