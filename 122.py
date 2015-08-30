#!/usr/bin/python -tt

# File:        p122.py
# Author:      Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2015-04-30
# Description: Project Euler problem 122

import sys
import re
import math
import pprint

def main():
  n = 200
  MAX = n + 1
  ways = [[[False for i in range(MAX)] for j in range(MAX)] for k in range(MAX)]
  ways[1][0][1] = True
  ways[2][1][1] = True
  ways[2][1][2] = True
  for i in range(3, MAX):
    for x in range(1, 1 + i/2):
      for y in range(5 * int(math.log(i))):
        if ways[i-x][y][x]:
          ways[i][y+1][x] = True
          ways[i][y+1][i - x] = True
          ways[i][y+1][i] = True
          ways[i][y+1][1] = True
  sol = 0
  # golden data
  s = [0, 0, 1, 2, 2, 3, 3, 4, 3, 4, 4, 5, 4, 5, 5, 5, 4, 5, 5, 6, 5, 6, 6, 6, 5, 6, 6, 6, 6, 7, 6, 7, 5, 6, 6, 7, 6, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 8, 6, 7, 7, 7, 7, 8, 7, 8, 7, 8, 8, 8, 7, 8, 8, 8, 6, 7, 7, 8, 7, 8, 8, 9, 7, 8, 8, 8, 8, 8, 8, 9, 7, 8, 8, 8, 8, 8, 8, 9, 8, 9, 8, 9, 8, 9, 9, 9, 7, 8, 8, 8, 8, 9, 8, 9, 8, 9, 9, 9, 8, 9, 9, 9, 8, 9, 9, 9, 9, 9, 9, 9, 8, 9, 9, 9, 9, 9, 9, 10, 7, 8, 8, 9, 8, 9, 9, 9, 8, 9, 9, 10, 9, 10, 10, 10, 8, 9, 9, 9, 9, 9, 9, 10, 9, 9, 9, 10, 9, 10, 10, 10, 8, 9, 9, 9, 9, 9, 9, 10, 9, 10, 9, 10, 9, 10, 10, 10, 9, 10, 10, 10, 9, 10, 10, 10, 9, 10, 10, 10, 10, 10, 10, 11, 8, 9, 9, 9, 9, 10, 9, 10, 9]
  for i in range(1, MAX):
    for j in range(1, MAX):
      if any(ways[i][j]):
         sol += j
         if j != s[i]:
             print i
         break
  print sol

if __name__ == '__main__':
  main()
