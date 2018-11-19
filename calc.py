#!/usr/bin/env python
import sys
a = float(sys.argv[1])
d = sys.argv[2]
b = float(sys.argv[3])

if d == '+':
    e = float(a + b)
elif d == '-':
    e = float(a - b)


elif d == '*':
    e = str(a * b)


elif d == '/':
    e = float(a / b)

print(e)
