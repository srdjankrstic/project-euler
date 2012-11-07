#!/usr/bin/python -tt

# File:        p023.py
# Author:      Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-11-03 14:44
# Description: Project Euler problem 23

import sys
import re
import math

def sumfactor(n):
  sol = 1
  for i in range(2, int(math.sqrt(n)) + 1):
    if not n % i:
      sol += i
      other = int(n/i)
      if i != other:
        sol += other
  return sol

def main():
  abundant = [False] * 28124
  abundants = []
  for i in range(1, 28124):
    if sumfactor(i) > i:
      abundants.append(i)
      abundant[i] = True

  sol = 0
  for i in range(1, 28124):
    issum = False
    for j in abundants:
      if i > j and abundant[i - j]:
        issum = True
        break
    if not issum:
      sol += i

  print sol

if __name__ == '__main__':
  main()
