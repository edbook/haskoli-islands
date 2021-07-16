#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Benedikt Magnusson <bsm@hi.is>
#
# Distributed under terms of the CC-BY-NC-SA license.

"""
Amit Saha: Doing Math With Python, page 14
Find the factors of an integer
"""


def factors(b):

    for i in range(1,b+1):
        if b % i == 0:
            print(i)

if __name__ == '__main__':
    try:
        b = input('Your number please:')
    except ValueError:
        print('Please enter a positive integer')
        b = 0

    b = float(b)

    if b>0 and b.is_integer():
        factors(int(b))
    else:
        print('Please enter a positive integer')
