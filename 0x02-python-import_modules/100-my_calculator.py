#!/usr/bin/python3

if __name__ == "__main":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)

    operator = argv[2]
    list_opr = {'+': add, '-': sub, '*': mul, '/': div}
    if operator not in list_opr:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    print('{:d} {:s} {:d} = {:d}'.format(a, operator, a, list_opr[operator](a, b)))
