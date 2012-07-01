#!/usr/bin/python -tt

# File:        p001.py
# Author:      Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-06-29 23:58
# Description: Project Euler problem 1

import sys
import re
import math

def main():
  print sum([n for n in range(1, 1000) if ((not n % 3) or (not n % 5))])

if __name__ == '__main__':
  main()
