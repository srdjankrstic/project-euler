#!/usr/bin/python -tt

# File:        p016.py
# Author:      Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-06-30 23:07
# Description: Project Euler problem 16

import sys
import re
import math

def main():
  digs = [1]
  for i in range(1000):
    carry = 0
    for j in range(len(digs)):
      digs[j] = digs[j] * 2 + carry
      if digs[j] >= 10:
        digs[j] -= 10
        carry = 1
      else:
        carry = 0
    if carry:
      digs.append(1)
  print sum(digs)

if __name__ == '__main__':
  main()
