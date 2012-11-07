#!/usr/bin/python -tt

# File:        p024.py
# Author:      Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-11-03 17:22
# Description: Project Euler problem 24

import sys
import re
import math

def main():
  leftover = 999999
  digits = []
  for i in range(9, -1, -1):
    cur = math.factorial(i)
    digits.append(leftover / cur)
    leftover %= cur
  
  alldigs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  for i in range(10):
    sys.stdout.write("%s" % alldigs[digits[i]])
    del alldigs[digits[i]]
  print

if __name__ == '__main__':
  main()
