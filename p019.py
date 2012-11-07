#!/usr/bin/python -tt

# File:        p019.py
# Author:      Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-07-02 11:30
# Description: Project Euler problem 19

import sys
import re
import math

NONLEAP = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
LEAP    = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def leap(year):
  return (not year % 400) if not year % 100 else (not year % 4)

def days(year, month):
  global NONLEAP
  global LEAP
  return LEAP[month] if leap(year) else NONLEAP[month]

def main():
  day = 2 # if Jan 1 1900 was Mon, Jan 1 1901 was Tue
  sundays = 0
  for year in range(1901, 2001):
    for month in range(12):
      if day == 0:
        sundays += 1
      day = (day + days(year, month)) % 7
  print sundays

if __name__ == '__main__':
  main()
