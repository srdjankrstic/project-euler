#!/usr/bin/python -tt

# File:        p027.py
# Author:      Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-11-07 00:02
# Description: Project Euler problem 27

import sys
import re
import math
import itertools

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
  best = 0
  prime = sieve(1000000)
  for b in [b for b in range(3, 1000, 2) if prime[b]]:
    for a in range(-999, 1000, 2):
      for n in itertools.count(1):
        res = n * n + a * n + b
        if res < 2 or not prime[res]:
          if n > best:
            best = n
            sol = a * b
          break
  print sol
  print best

if __name__ == '__main__':
  main()
