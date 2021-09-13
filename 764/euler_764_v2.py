#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 Shlomi Fish < https://www.shlomifish.org/ >
#
# Licensed under the terms of the MIT license.

"""

"""

from math import gcd, sqrt


def g(x, y, z):
    return gcd(gcd(x, y), z) == 1


def issq(xsq):
    x = int(sqrt(xsq))
    if x*x == xsq:
        return x
    else:
        return None


def calc_sum_S(N):
    ret = 0
    m = 1
    c = 0
    while True:
        if not m & 0xFFF:
            print(N, c, ret, flush=True)
        m += 1
        m2 = m*m
        # startn = (2 if m & 1 else 1)
        for n in range(1, m):
            n2 = n*n
            a = m2 - n2
            b = 2*m*n
            c = m2 + n2
            if c > N:
                if n == 1:
                    return ret
                break
            y = issq(a)
            if y:
                if 0 == (b & 3):
                    x = b >> 2
                    if g(x, y, c):
                        ret += x + y + c
            a, b = b, a
            y = issq(a)
            if y:
                if 0 == (b & 3):
                    x = b >> 2
                    if g(x, y, c):
                        ret += x + y + c


def test1():
    assert calc_sum_S(100) == 81
    assert calc_sum_S(10 ** 4) == 112851
    # print(calc_sum_S(10 ** 6))
    # return
    assert calc_sum_S(10 ** 7) % (10 ** 9) == 248876211
    res = calc_sum_S(10 ** 16)
    print(res)
    print(res % (10 ** 9))


test1()
