#!/usr/bin/python3
for k in range(ord('z'), ord('a') - 1, -1):
    if k % 2 == 0:
        diff = 0
    else:
        diff = 32
    print('{}'.format(chr(k - diff)), end='')
