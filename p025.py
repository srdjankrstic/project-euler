#!/usr/bin/python -tt

# File:        p025.py
# Author:      Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-11-03 17:37
# Description: Project Euler problem 25

import sys
import re
import math

def main():
  fib1 = 1
  fib2 = 1
  index = 3
  while True:
    fibold = fib1
    fib1 = fib2
    fib2 += fibold
    if math.log(fib2, 10) > 999:
      break
    index += 1
  print index

if __name__ == '__main__':
  main()
