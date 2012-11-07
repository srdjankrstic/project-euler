#!/usr/bin/python -tt

# File:        p031.py
# Author:      Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-11-07 01:17
# Description: Project Euler problem 31

import sys
import re
import math

def main():
  denom = [1, 2, 5, 10, 20, 50, 100, 200]
  ways = [0] * 201
  ways[0] = 1
  for j in denom:
    for i in range(201):
      if i - j >= 0:
        ways[i] += ways[i - j]
  print ways[200]

if __name__ == '__main__':
  main()
