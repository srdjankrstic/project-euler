#!/usr/bin/python -tt

# File:        p005.py
# Author:      Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-06-30 15:52
# Description: Project Euler problem 5

import sys
import re
import math

def gcd(a, b):
  if b > a:
    return gcd(b, a)
  if b == 0:
    return a
  return gcd(b, a % b)

def main():
  num = 1
  for i in range(1, 21):
    num *= i / gcd(num, i)
  print num

if __name__ == '__main__':
  main()
