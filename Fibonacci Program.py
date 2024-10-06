# fibonacci.py
a, b = 1, 1
while a < 1000:
    print(a, end=", ")
    a, b = b, a + b

# fibonacci_ratios.py
a, b = 1, 1
while b < 1000:
    ratio = b / a
    print(ratio)
    a, b = b, a + b

#1.618 is a golden ratio
