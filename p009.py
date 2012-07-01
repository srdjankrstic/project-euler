#!/usr/bin/python -tt

# File:        p009.py
# Author:      Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-06-30 16:20
# Description: Project Euler problem 9

import sys
import re
import math

def main():
  for c in range(1, 500):
    c2 = c * c
    for a in range(1, c):
      b = 1000 - c - a
      if a * a + b * b == c2:
        sol = a * b * c
        break
  print sol

if __name__ == '__main__':
  main()
