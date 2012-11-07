#!/usr/bin/python -tt

# File:        p022.py
# Author:      Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-11-02 18:05
# Description: Project Euler problem 22

import sys
import re
import math

def score(name):
  score = 0
  for c in name:
    score += ord(c) - ord('A') + 1
  return score

def main():
  with open('names.txt', 'r') as f:
    slist = [score(name) for name in sorted([x[1:-1] for x in f.readline().split(',')])]
    print sum((i + 1) * slist[i] for i in range(len(slist)))

if __name__ == '__main__':
  main()
