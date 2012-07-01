#!/usr/bin/python -tt

# File: 	     p002.py
# Author: 	   Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-06-29 23:58
# Description: Project Euler problem 2

import sys
import re
import math

def main():
  sum = 0
  f1 = 1
  f2 = 1
  while f2 < 4000000:
  	if f2 % 2 == 0:
  	  sum += f2
  	temp = f2
  	f2 += f1
  	f1 = temp
  print sum

if __name__ == '__main__':
	main()
