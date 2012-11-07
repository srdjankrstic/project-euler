#!/usr/bin/python -tt

# File:        p029.py
# Author:      Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-11-07 00:41
# Description: Project Euler problem 29

import sys
import re
import math

def main():
  print len(set([math.pow(a, b) for a in range(2, 101) for b in range(2, 101)]))

if __name__ == '__main__':
  main()
