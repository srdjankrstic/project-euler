#!/usr/bin/python -tt

# File:        p014.py
# Author:      Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-06-30 22:31
# Description: Project Euler problem 14

import sys
import re
import math

def collatz(n):
  if n == 1:
    return 1
  if n < 3000000 and STEPS[n] > 0:
    return STEPS[n]
  if not n % 2:
    x = 1 + collatz(n // 2)
    if n < 3000000:
      STEPS[n] = x
    return x
  else:
    x = 1 + collatz(3 * n + 1)
    if n < 3000000:
      STEPS[n] = x
    return x

def main():
  global STEPS
  STEPS = [0] * 3000000
  max = 1
  for i in range(1000000):
    if collatz(i + 1) > collatz(max):
      max = i + 1
  print max

if __name__ == '__main__':
  main()
