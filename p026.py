#!/usr/bin/python -tt

# File:        p026.py
# Author:      Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-11-06 23:45
# Description: Project Euler problem 26

import sys
import re
import math

def seqlen(x):
  currem = 10
  seen = [0] * 10000
  i = 1
  while currem != 0 and not seen[currem]:
    seen[currem] = i
    currem = currem % x
    currem *= 10
    i += 1
  return 0 if currem == 0 else i - seen[currem]

def main():
  maxlen, maxi = max((seqlen(i + 1), i + 1) for i in range(1000))
  print maxi

if __name__ == '__main__':
  main()
