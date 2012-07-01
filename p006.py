#!/usr/bin/python -tt

# File: 	     p006.py
# Author: 	   Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-06-30 15:56
# Description: Project Euler problem 6

import sys
import re
import math

def main():
  n = 100
  sum1 = n * (n + 1) / 2
  sum2 = n * (n + 1) * (2 * n + 1) / 6
  print sum1 * sum1 - sum2

if __name__ == '__main__':
	main()
