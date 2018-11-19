#!/usr/bin/env python
import sys
# print(sys.argv)
a = float(sys.argv[1])
d = sys.argv[2]
b = float(sys.argv[3])

#a = float(raw_input("Vvedite pervoe chislo = ",))
#d = str(raw_input("Vvedite operator (+, -, *, /) = "))
#b = float(raw_input("Vvedite vtoroe chislo = ",))


if d == '+':
    e = float(a + b)
elif d == '-':
    e = float(a - b)


elif d == '*':
    e = str(a * b)


elif d == '/':
    e = float(a / b)

print(e)
