#!/usr/bin/python -tt

# File:        p030.py
# Author:      Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-11-07 01:05
# Description: Project Euler problem 30

import sys
import re
import math

def works(x):
  sumfifth = 0
  y = x
  while y > 0:
    sumfifth += (y % 10) ** 5
    y /= 10
  return sumfifth == x

def main():
  print sum([x for x in xrange(10, 6 * 9 ** 5 + 1) if works(x)])

if __name__ == '__main__':
  main()
