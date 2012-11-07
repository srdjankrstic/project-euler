#!/usr/bin/python -tt

# File:        p017.py
# Author:      Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-07-02 10:47
# Description: Project Euler problem 17

import sys
import re
import math

def chars(n):
  if n == 0:
    return 0
  if n in [1, 2, 6, 10]:
    return 3
  elif n in [4, 5, 9]:
    return 4
  elif n in [3, 7, 8, 40, 50, 60]:
    return 5
  elif n in [11, 12, 20, 30, 80, 90]:
    return 6
  elif n in [15, 16, 70]:
    return 7
  elif n in [13, 14, 18, 19]:
    return 8
  elif n in [17]:
    return 9
  elif n < 100:
    return chars(10 * (n // 10)) + chars(n % 10)
  elif n < 1000:
    return chars(n // 100) + 7 + (3 if n % 100 else 0) + chars(n % 100) # 7 is "hundred," 3 for "and"
  else:
    return chars(n // 1000) + 8 + chars(n % 1000) # 8 for "thousand"

def main():
  # print sum(chars(x) for x in range(6)) # 19
  # print chars(342)                      # 23
  # print chars(115)                      # 20
  print sum(chars(x) for x in range(1001))
  
if __name__ == '__main__':
  main()
