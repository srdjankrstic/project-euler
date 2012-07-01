#!/usr/bin/python -tt

# File:        p003.py
# Author:      Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-06-30 00:08
# Description: Project Euler problem 3

import sys
import re
import math

def main():
  num = 600851475143
  ceil = int(math.sqrt(num))
  maxd = 1
  for div in range(2, ceil + 1):
    if not num % div:
      while not num % div:
        num /= div
      if div > maxd:
        maxd = div
    if num == 1:
      break
  print maxd if num == 1 else num

if __name__ == '__main__':
  main()
