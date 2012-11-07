#!/usr/bin/python -tt

# File:        p028.py
# Author:      Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-11-07 00:27
# Description: Project Euler problem 28

import sys
import re
import math

def main():
  sol = 0
  cur = 1
  step = 0
  i = 0
  while cur <= 1001 * 1001:
    sol += cur
    if not i % 4:
      step += 2
    i += 1
    cur += step
  print sol


if __name__ == '__main__':
  main()
