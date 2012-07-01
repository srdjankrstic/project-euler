#!/usr/bin/python -tt

# File:        p010.py
# Author:      Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-06-30 16:24
# Description: Project Euler problem 10

import sys
import re
import math

def sieve(n):
  prime = [False, True] * (n // 2 + 1)
  prime[1] = False
  prime[2] = True
  for i in xrange(3, int(math.sqrt(n + 1)), 2):
    if prime[i]:
      for j in xrange(i * i, n + 1, 2 * i):
        prime[j] = False
  return prime

def main():
  prime = sieve(2000000)
  print sum([x for x in range(2000001) if prime[x]])

if __name__ == '__main__':
  main()
