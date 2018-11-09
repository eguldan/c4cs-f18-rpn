#!/usr/bin/env python3

#from decimal import *

def calculate(arg):
    stack = []

    tokens = arg.split()

    for token in tokens:
        try:
            stack.append(int(token))
        except ValueError:
            if token == 'sum':
                result = 0
                while len(stack) > 0:
                    result = result + stack.pop()
            elif token == '!':
                val1 = stack.pop()
                if val1 == 0:
                    result = 1
                else:
                    result = val1
                    while val1 > 1:
                        result = result * (val1 - 1)
                        val1 = val1 - 1
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                if token == '+':
                    result = val1 + val2
                elif token == '-':
                    result = val1 - val2
                elif token == '%':
                    result = round(((val1 / 100) * val2), 1)  
                elif token == '^':
                    result = val1 ** val2
                elif token == '//':
                    result = val1 // val2

            stack.append(result)
    
    if len(stack) > 1:
        raise ValueError('Too many arguments on the stack')
    
    return stack[0]

def main():
    #dP = input("enter dP: ")
    #getcontext().prec = int(dP)
    
    while True:
        try:
            result = calculate(input("rpn calc> "))
            print(result)
        except ValueError:
            pass

if __name__ == '__main__':
    main()

