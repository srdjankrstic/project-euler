#!/usr/bin/python -tt

# File:        p012.py
# Author:      Srdjan Krstic (krstic.m.srdjan@gmail.com)
# Created:     2012-06-30 17:59
# Description: Project Euler problem 12

import sys
import re
import math

def sieve(n):
  prime = [False, True] * (n // 2 + 1)
  prime[1] = False
  prime[2] = True
  for i in xrange(3, int(math.sqrt(n + 1)), 2):
    if prime[i]:
      for j in xrange(i * i, n + 1, 2 * i):
        prime[j] = False
  return prime

def divisors(n):
  "returns the number of divisors of a number using the standard formula"
  # uses the formula d(n) = \\prod (a_i + 1) if n = \\prod p_i^(a_i) is the prime factorization
  if (divisors.mem[n] > 0):
    return divisors.mem[n]
  orig = n
  divisors.mem[1] = 1
  for prime in divisors.primes:
    exp = 0
    while n > 0 and not n % prime:
      exp += 1
      n /= prime
    if exp > 0:
      divisors.mem[orig] = divisors.mem[n] * (exp + 1)
      return divisors.mem[orig]
  return 2

# memoize the divisor function values for speed
divisors.mem = [0] * 1000000 

# calculate primes once into a static array in divisors
# there must be a more python-y way of doing this
ps = sieve(10000)
divisors.primes = []
for i in range(10000):
  if ps[i]:
    divisors.primes.append(i)

def main():
  for i in range(4, 1000000, 2):
    # triangle numbers are of form n(n+1)/2. n and (n + 1) are always coprime,
    # and so they also are when one is divided by 2 so the divisor function
    # is then multiplicative
    if divisors(i / 2) * divisors(i - 1) > 500:
      print i * (i - 1) / 2
      return
    elif divisors(i / 2) * divisors(i + 1) > 500:
      print i * (i + 1) / 2
      return

if __name__ == '__main__':
  main()
