#!/usr/bin/python -tt

# File: 	     p004.py
# Author: 	   Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-06-30 00:16
# Description: Project Euler problem 4

import sys
import re
import math

def main():
	max = 0
	for n1 in range(100, 1000):
		for n2 in range(100, 1000):
			prod = n1 * n2
			s = str(prod)
			if s == s[::-1] and prod > max:
				max = prod
	print max

if __name__ == '__main__':
	main()
