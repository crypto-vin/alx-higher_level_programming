#!/usr/bin/python3

import hidden_4

def myfunc():
    array = dir(hidden_4)
    for element in array:
        if not element.startswith('__'):
            print(element)

if __name__ == '__main__':
    myfunc()
