a = float(raw_input("Vvedite pervoe chislo =",))
d = str(raw_input("Vvedite operator (+, -, *,/) ="))
b = float(raw_input("Vvedite vtoroe chislo =",))

if d == '+':
    e = float(a + b)
elif d == '-':
    e = float(a - b)


elif d == '*':
    e = str(a * b)


elif d == '/':
    e = float(a / b)

print(e)
