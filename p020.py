#!/usr/bin/python -tt

# File:        p020.py
# Author:      Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-07-02 11:54
# Description: Projcet Euler problem 20

import sys
import re
import math

def main():
  print sum(int(dig) for dig in str(math.factorial(100)))

if __name__ == '__main__':
  main()
