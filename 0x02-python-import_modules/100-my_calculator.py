#!/usr/bin/python3
"""Program imports all functions from calculator_1.py and handles basic operations"""

if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv[1:]) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a, b, c = sys.argv[1], sys.argv[2], sys.argv[3]

    if b == '+':
        print("{} + {} = {}".format(a, c, add(int(a), int(c))))

    elif b == '-':
        print("{} - {} = {}".format(a, c, sub(int(a), int(c))))

    elif b == '*':
        print("{} * {} = {}".format(a, c, mul(int(a), int(c))))

    elif b == '/':
        print("{} / {} = {}".format(a, c, div(int(a), int(c))))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
