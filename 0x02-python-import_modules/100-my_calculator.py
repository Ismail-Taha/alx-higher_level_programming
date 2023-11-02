#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)

    opr = argv[2]
    ls_opr = {'+': add, '-': sub, '*': mul, '/': div}
    if opr not in ls_opr:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    print('{:d} {:s} {:d} = {:d}'.format(a, opr, b, ls_opr[opr](a, b)))
