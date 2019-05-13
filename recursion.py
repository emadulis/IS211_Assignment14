#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Recursion module."""


def fibonacci(n):

    if n == 1:
        return 1
    if n == 0:
        return 0

    return fibonacci(n-2) + fibonacci(n-1)


def gcd(num1, num2):

    if num2 == 0:
        return num1

    return gcd(num2, (num1 % num2))


def comparrison(s1, s2):

    sample1 = s1[1:2]
    sample2 = s2[1:2]

    if len(sample1) == 0 and len(sample2) != 0:
        return -1
    elif len(sample1) != 0 and len(sample2) == 0:
        return 1
    elif len(sample1) == 0 and len(sample2) == 0:
        return 0

    if ord(sample1) < ord(sample2):
        return -1
    elif ord(sample1) > ord(sample2):
        return 1

    return comparrison(s1[1:], s2[1:])


def main():

    print "Please choose a recusrive function:\n" \
          "1 FIBONACCI\n" \
          "2 GCD\n" \
          "3 comparrison\n"
    try:
        while True:
            decision = int(raw_input("\nYour choice: "))

            if decision == 1:
                pos = int(
                    raw_input("Please pick a position in the Fibonacci Sequence "))
                print "Answer: ", fibonacci(pos)
            elif decision == 2:
                n1 = int(raw_input("num 1: "))
                n2 = int(raw_input("num 2: "))
                print "Answer: ", gcd(n1, n2)
            elif decision == 3:
                str1 = raw_input("String 1: ")
                str2 = raw_input("String 2: ")
                print "Response: ", comparrison(str1, str2)
            elif decision < 1 or decision > 3:
                print "Please enter 1, 2, or 3."

    except ValueError:
        print "Invalid selection, please select a vaid option"


if __name__ == "__main__":
    main()
