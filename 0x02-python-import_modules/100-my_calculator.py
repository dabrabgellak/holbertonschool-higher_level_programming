#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    argc = len(sys.argv)

    if argc != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    c = sys.argv[2]

    if c != '+' and c != '-' and c != '/' and c != '*':
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    elif c == '+':
        print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
    elif c == '-':
        print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
    elif c == '*':
        print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
    elif c == '/':
        print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
