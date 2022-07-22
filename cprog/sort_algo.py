#!/usr/bin/python3.5 -tt


"""
Author Nav Don
"""
import os
import time
import random
import re
import sys




def main():
    print('Enter preferred sorting algorithim')
    sort_type = input('1 - bubblesort | 2 - insertsort | 3 - selection sort\n')
    print('Enter size of array\n')
    sort_size = int(input('1 - five elements | 2 - 20 elements | 3 - 50 elements | 4 - 100 elemnts | 1000 elements'))
    array = []
    for i in range(0, sort_size):
        while True:
            value = [random.randint(0, sort_size)]
            if value in array:
                continue
            else:
                element.append(value)
    print(array)




if __name__ == '__main__':
        main()

