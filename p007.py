#!/usr/bin/python -tt

# File:        p007.py
# Author:      Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-06-30 16:04
# Description: Project Euler problem 7

import sys
import re
import math

def main():
  primes = [2]
  num = 3
  count = 1
  while count < 10001:
    prime = True
    max = int(math.sqrt(num))
    for i in primes:
      if i > max:
        break
      if not num % i:
        prime = False
        break
    if prime:
      primes.append(num)
      count += 1
    num += 2
  print primes[-1]

if __name__ == '__main__':
  main()
