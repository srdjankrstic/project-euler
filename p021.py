#!/usr/bin/python -tt

# File:        p021.py
# Author:      Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-11-02 17:30
# Description: Project Euler problem 21

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
  sol = 0
  amic = [False] * 10001
  sumdiv = [sumfactor(i) for i in range(10001)]
  for i in range(1, 10001):
    if sumdiv[i] <= 10000 and i != sumdiv[i] and sumdiv[sumdiv[i]] == i:
      if not amic[i]:
        amic[i] = True
        sol += i
      if not amic[sumdiv[i]]:
        amic[sumdiv[i]] = True
        sol += sumdiv[i]
  print sol

if __name__ == '__main__':
  main()
